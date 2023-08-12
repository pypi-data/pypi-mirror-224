from datetime import datetime
from functools import wraps
from django.contrib.auth import get_user_model, login
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.http import HttpRequest
from django.utils import timezone
from .app_settings import app_settings
from .models import SimulatedUserSession, SimulatedUserAction


UserModel = get_user_model()


def reset_real_user(view_func: any = None, *, request: HttpRequest | None = None):
    """
    Decorator function to reset the 'real_user' attribute on the request object.
    If used without arguments, it will also reset 'simulated_user_pk' if it exists.

    Args:
    - view_func: View function to be wrapped.
    - request: The request object.

    Returns:
    - Function: The wrapped function or the decorator itself.
    """
    # noinspection PyShadowingNames
    def decorator(view_func):
        # noinspection PyShadowingNames
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            request.real_user = request.user
            if getattr(request,  'simulated_user_pk', None):
                request.simulated_user_pk = None
            return view_func(request, *args, **kwargs)
        return _wrapped_view

    if view_func is not None:
        return decorator(view_func)

    if request is not None:
        request.real_user = request.user
        if getattr(request, 'simulated_user_pk', None):
            request.simulated_user_pk = None


# noinspection PyProtectedMember
def new_simulated_session(request: HttpRequest, hide_bar: bool = False) -> HttpRequest:
    """
    Create a new simulated session for the user.

    Args:
    - request: The request object.
    - hide_bar: Boolean indicating if the simulation bar should be hidden.

    Returns:
    - HttpRequest: Modified request object.
    """
    control_condition: bool = getattr(request.real_user, app_settings.MIMICRY_FEATURE_CONTROL_CONDITION, False)
    request.simulated_user_pk = getattr(request, 'simulated_user_pk', None)
    if control_condition and request.simulated_user_pk:
        real_session_key: str | None = request.session.session_key
        if not (request.simulated_user_pk == 'unauthenticated' or request.simulated_user_pk is None):
            request.session['_auth_user_id'] = request.simulated_user_pk

        simulated_session: SimulatedUserSession = SimulatedUserSession()
        simulated_session.real_user = request.real_user
        if hide_bar:
            request: HttpRequest = change_user(request, request.real_user)
            simulated_session.hide_bar = True
            simulated_session.closed_at = timezone.now()
        else:
            if request.simulated_user_pk == 'unauthenticated':
                request: HttpRequest = change_user(request, AnonymousUser())
            else:
                try:
                    primary_key_field: str = UserModel._meta.pk.name
                    filter_kwargs: dict[str, str] = {primary_key_field: request.simulated_user_pk}
                    user_to_login: UserModel | AnonymousUser = UserModel.objects.get(**filter_kwargs)
                    request: HttpRequest = change_user(request, user_to_login)
                except UserModel.DoesNotExist:
                    request: HttpRequest = change_user(request, AnonymousUser())
            if isinstance(request.user, AnonymousUser):
                simulated_session.simulated_user = None
            else:
                simulated_session.simulated_user = request.user
        simulated_session.real_session_key = real_session_key
        simulated_session.simulated_session_key = request.session.session_key
        try:
            simulated_session.save()
        except IntegrityError:
            pass

    return request


def set_hide_bar(request: HttpRequest, hide_bar_status: bool = True) -> HttpRequest:
    """
    Sets the 'hide_bar' status for the current simulated session.

    Args:
    - request: The request object.
    - hide_bar_status: Boolean indicating the desired 'hide_bar' status.

    Returns:
    - HttpRequest: Modified request object.
    """
    control_condition: bool = getattr(request.real_user, app_settings.MIMICRY_FEATURE_CONTROL_CONDITION, False)
    if control_condition:
        try:
            simulated_session: SimulatedUserSession = SimulatedUserSession.objects.get(
                simulated_session_key=request.session.session_key, closed_at__isnull=True
            )
            simulated_session.closed_at = timezone.now()
            simulated_session.hide_bar = hide_bar_status
            simulated_session.save()
        except SimulatedUserSession.DoesNotExist:
            request.simulated_user_pk = 'unauthenticated'
            request: HttpRequest = new_simulated_session(request, hide_bar=True)
    return request


def disable_bar(request: HttpRequest) -> HttpRequest:
    """
    Disables the simulation bar and ends the current simulated session.

    Args:
    - request: The request object.

    Returns:
    - HttpRequest: Modified request object.
    """
    control_condition: bool = getattr(request.real_user, app_settings.MIMICRY_FEATURE_CONTROL_CONDITION, False)
    if control_condition:
        try:
            simulated_session: SimulatedUserSession = SimulatedUserSession.objects.get(
                simulated_session_key=request.session.session_key, closed_at__isnull=True
            )
            simulated_session.closed_at = timezone.now()
            simulated_session.save()
            request.real_user = simulated_session.real_user
            request: HttpRequest = change_user(request, request.real_user)
            request.simulation_created_at = None
        except SimulatedUserSession.DoesNotExist:
            pass
    return request


def coordinate_request_with_simulated_session(request: HttpRequest) -> HttpRequest:
    """
    Coordinate the request with the currently active simulated session.

    Args:
    - request: The request object.

    Returns:
    - HttpRequest: Modified request object.
    """
    request.real_user = getattr(request, 'real_user', request.user)
    _is_simulated_user_session: bool = request.session.get('_is_simulated_user_session', False)
    if app_settings.ENABLE_MIMICRY:
        session_key: str = request.session.session_key
        if _is_simulated_user_session:
            simulated_session: SimulatedUserSession = SimulatedUserSession.objects.filter(
                simulated_session_key=session_key
            ).first()
            if simulated_session and simulated_session.closed_at:
                request.real_user = simulated_session.real_user
                simulated_session: None = None

            if simulated_session:
                simulated_session.save()
                active_simulated_session: SimulatedUserSession = SimulatedUserSession.objects.filter(
                    simulated_session_key=session_key, closed_at__isnull=True
                ).first()
                if active_simulated_session and not simulated_session.hide_bar:
                    request.real_user = active_simulated_session.real_user
                    if active_simulated_session.simulated_user is None:
                        request: HttpRequest = change_user(request, AnonymousUser())
                        log_simulated_action(
                            request,
                            active_simulated_session,
                            f"{request.real_user.username} simulating AnonymousUser accessed {request.path}"
                        )
                    else:
                        request: HttpRequest = change_user(request, active_simulated_session.simulated_user)
                        log_simulated_action(
                            request,
                            active_simulated_session,
                            f"{request.real_user.username} simulating user: {request.user.username} accessed"
                            f" {request.path}"
                        )
                    request.simulation_created_at = active_simulated_session.created_at
                else:
                    request.real_user = simulated_session.real_user
                    request: HttpRequest = change_user(request, request.real_user)
                    request.simulation_created_at = None
            else:
                request: HttpRequest = change_user(request, request.real_user)
                request.simulation_created_at = None
        else:
            request: HttpRequest = change_user(request, request.real_user)
            request.simulation_created_at = None
    else:
        request: HttpRequest = change_user(request, request.real_user)
        request.simulation_created_at = None

    return request


def change_user(request: HttpRequest, user: UserModel | AnonymousUser) -> HttpRequest:
    """
    Change the user of the current request.

    Args:
    - request: The request object.
    - user: The user object or AnonymousUser to be set on the request.

    Returns:
    - HttpRequest: Modified request object.
    """
    if request.user != user:
        real_user: UserModel | AnonymousUser = getattr(request, 'real_user', request.user)
        simulation_created_at: datetime | None = getattr(request, 'simulation_created_at', None)
        simulated_user_pk: str | None = getattr(request, 'simulated_user_pk', None)
        if isinstance(user, UserModel):
            if check_user_simulation_permissions(request.real_user, user):
                user.backend = app_settings.MIMICRY_AUTHENTICATION_BACKEND
                login(request, user)
                request.session.save()
            else:
                raise PermissionDenied("You don't have permission to access this user.")
        else:
            if check_user_simulation_permissions(request.real_user, AnonymousUser()):
                request.session.clear()
                request.session.create()
                request.user = AnonymousUser()
            else:
                raise PermissionDenied("You don't have permission to access this user.")
        request.real_user = real_user
        request.simulation_created_at = simulation_created_at
        request.simulated_user_pk = simulated_user_pk
        request.session["_is_simulated_user_session"] = True

    return request


def check_user_simulation_permissions(real_user: UserModel, simulated_user: UserModel) -> bool:
    if isinstance(real_user, UserModel):
        if isinstance(simulated_user, UserModel) or isinstance(simulated_user, AnonymousUser):
            if isinstance(simulated_user, AnonymousUser):
                return True
            else:
                permission_settings: list[dict[str, str]] = app_settings.MIMICRY_PERMISSIONS
                permission_settings.append(
                    {"SIMULATED_USER_ATTRIBUTE": "_ALWAYS_TRUE", "REAL_USER_ATTRIBUTE": "is_staff"}
                )
                for setting in permission_settings:
                    simulated_user_attribute: str = setting["SIMULATED_USER_ATTRIBUTE"]
                    real_user_attribute: str = setting["REAL_USER_ATTRIBUTE"]
                    if simulated_user_attribute == "_ALWAYS_TRUE":
                        simulated_user_attribute_results: bool = True
                    else:
                        simulated_user_attribute_results = getattr(simulated_user, simulated_user_attribute, None)
                        if type(simulated_user_attribute_results) is not bool:
                            raise TypeError(f"Did not find {simulated_user_attribute} to be bool for simulated_user")
                    real_user_attribute_results = getattr(real_user, real_user_attribute, None)
                    if type(real_user_attribute_results) is not bool:
                        raise TypeError(f"Did not find {real_user_attribute_results} to be bool for real_user")
                    if simulated_user_attribute_results:
                        return real_user_attribute_results
                    else:
                        continue

        else:
            raise TypeError("simulated_user must be an instance of your user model or AnonymousUser")
    else:
        raise TypeError("real_user must be an instance of your user model")


def log_simulated_action(
        request: HttpRequest, simulated_session_instance: SimulatedUserSession, action_desc: str
) -> None:
    """
    Log an action performed during a simulated session.

    Args:
    - request: The request object.
    - simulated_session_instance: Instance of the current simulated session.
    - action_desc: Description of the action performed.

    Returns:
    - None
    """
    if request.real_user != request.user:
        try:
            simulated_user_action = SimulatedUserAction.objects.create(
                simulated_user_session=simulated_session_instance,
                action=action_desc
            )
            simulated_user_action.save()
        except SimulatedUserSession.DoesNotExist:
            pass
