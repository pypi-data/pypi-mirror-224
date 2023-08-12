from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from .app_settings import app_settings
from .models import SimulatedUserSession


@receiver(post_save, sender=SimulatedUserSession)
def send_simulation_notification(sender, instance, created, **kwargs) -> None:
    """
    Sends an email notification to the real user when a new simulated user session is created.

    This function is connected to the post_save signal of the SimulatedUserSession model.
    It is triggered every time an instance of this model is saved. The function checks
    if this is a new record and, if so, prepares and sends an email notification to the real user.

    Parameters:
    - sender: The model class. (SimulatedUserSession in this case)
    - instance: The actual instance being saved.
    - created: Boolean indicating whether this instance is being created.
               If it's an update to an existing instance, created is False.
    - **kwargs: Additional keyword arguments.

    Email Templates Used:
    - 'simulateuser/simulation_email_subject.txt': Used for the email subject.
    - 'simulateuser/simulation_email.txt': Used for the plain text content of the email.
    - 'simulateuser/simulation_email.html': Used for the HTML content of the email.

    The templates will be rendered with a context containing the following variables:
    - real_user: The actual user who initiated the simulation.
    - simulated_user: The user being simulated.
    - timestamp: The time when the simulation started.
    """

    if created and app_settings.ENABLE_SIMULATE_USER_NOTIFICATIONS:  # Check if this is a new record
        context: dict[str, any] = {
            'real_user': instance.real_user,
            'simulated_user': instance.simulated_user,
            'timestamp': instance.created_at
        }

        # Render the email subject and contents using the specified templates and context
        subject: str = render_to_string('mimicry/simulation_email_subject.txt', context).strip()
        text_content: str = render_to_string('mimicry/simulation_email.txt', context)
        html_content: str = render_to_string('mimicry/simulation_email.html', context)

        # Create a multipart email with both plain text and HTML content
        email: EmailMultiAlternatives = EmailMultiAlternatives(
            subject, text_content, settings.EMAIL_HOST_USER, [instance.real_user.email]
        )
        email.attach_alternative(html_content, "text/html")

        # Send the email
        email.send()
