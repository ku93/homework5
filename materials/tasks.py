from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


@shared_task
def send_information_subscription(email):
    """Отправляет сообщение пользователям имеющие подписку об изменении курса"""
    send_mail("Курс обновлен", "Ваш курс обновлен", EMAIL_HOST_USER, [email])
