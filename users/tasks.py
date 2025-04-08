from datetime import timedelta
from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils import timezone

from config.settings import EMAIL_HOST_USER


@shared_task
def deactivate_inactive_users():
    """Блокирует пользователей, которые не заходили более месяца."""
    one_month_ago = timezone.now() - timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=one_month_ago, is_active=True)

    email_list = []

    for user in inactive_users:
        email_list.append(user.email)
        user.is_active = False
        user.save()
        if email_list:
            send_mail(
                "Ваша учетная запись заблокирована",
                """Здравствуйте!
            Мы хотим сообщить вам, что ваша учетная запись была временно заблокирована. 
            Это решение было принято в связи с тем, что вы не входили в систему в течение длительного времени.
            Если вы считаете, что это ошибка или у вас есть вопросы, пожалуйста, свяжитесь с нашей службой поддержки 
            Мы ценим вашу активность и надеемся снова увидеть вас
            """,
                EMAIL_HOST_USER,
                email_list,
            )

        print(f"Пользователь {user.username} был заблокирован.")
