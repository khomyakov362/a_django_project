from django.conf import settings
from django.core.mail import send_mail

def send_register_email(email):
    send_mail(
        subject='Registration',
        message='You have been successully registered on or service: Shelter.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )

def send_new_password(email, new_password):
    send_mail(
        subject='New password',
        message=f'You have changed your password to: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
