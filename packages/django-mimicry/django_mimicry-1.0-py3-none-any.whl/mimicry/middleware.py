from django.http import HttpResponseForbidden, HttpRequest, HttpResponse
from django.urls import reverse
from .app_settings import app_settings
from .utils import coordinate_request_with_simulated_session


class SimulateUserMiddleware:
    """
    Middleware to facilitate the user simulation feature.

    This middleware performs two main functions:
    1. Coordinates the request with the simulated user session, ensuring that
       `request.user` is set to the simulated user and `request.real_user` is set to the actual user.
    2. If ONLY_ALLOW_SIMULATED_GET_AND_HEAD_REQUESTS setting is enabled, ensures that
       only GET and HEAD requests are allowed during user simulation except for the 'mimicry_switch_user' endpoint.

    Attributes:
    - get_response: A callable to get the response using the provided request.

    Methods:
    - __call__: Method that gets executed for each request before reaching the view.
    """

    def __init__(self, get_response) -> None:
        """
        Initializes the middleware.

        Args:
        - get_response: A callable which takes a request and returns a response.
                        It could be the next middleware in line or the final view.
        """
        self.get_response = get_response

    # noinspection PyProtectedMember
    def __call__(self, request: HttpRequest) -> HttpResponseForbidden | HttpResponse:
        """
        Method that gets executed for each request before it reaches the view.

        Args:
        - request: The current request instance.

        Returns:
        - A HttpResponse object.
        """

        # Update the request with the simulated user's session details.
        request: HttpRequest = coordinate_request_with_simulated_session(request)

        # Check if ONLY_ALLOW_SIMULATED_GET_REQUESTS setting is enabled
        # and block non-GET requests during user simulation.
        # The 'simulate_user_switch_user' endpoint is exempted.
        if app_settings.ONLY_ALLOW_SIMULATED_GET_AND_HEAD_REQUESTS:
            if (
                request.method not in ["GET", "HEAD"] and
                request.real_user != request.user and
                not request.path.startswith(reverse('mimicry_switch_user'))
            ):
                return HttpResponseForbidden("Only GET and HEAD requests allowed in simulation mode")

        # Continue processing and get the response
        response: HttpResponse = self.get_response(request)
        return response
