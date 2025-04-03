from datetime import datetime

from django.core.management.base import BaseCommand

from materials.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    help = "Заполняет таблицу Payment тестовыми данными"

    def handle(self, *args, **kwargs):

        user1 = User.objects.get(id=1)
        user2 = User.objects.get(id=2)
        course1 = Course.objects.get(id=1)
        course2 = Course.objects.get(id=2)
        lesson1 = Lesson.objects.get(id=1)
        lesson2 = Lesson.objects.get(id=2)
        lesson3 = Lesson.objects.get(id=3)

        # Создаем платежи
        Payment.objects.create(
            user=user1,
            payment_date=datetime.now(),
            paid_course=course1,
            paid_lesson=None,
            amount=100.00,
            payment_method="cash",
        )

        Payment.objects.create(
            user=user2,
            payment_date=datetime.now(),
            paid_course=None,
            paid_lesson=lesson1,
            amount=50.00,
            payment_method="transfer",
        )

        Payment.objects.create(
            user=user1,
            payment_date=datetime.now(),
            paid_course=course2,
            paid_lesson=None,
            amount=200.00,
            payment_method="cash",
        )

        Payment.objects.create(
            user=user2,
            payment_date=datetime.now(),
            paid_course=None,
            paid_lesson=lesson3,
            amount=75.00,
            payment_method="transfer",
        )

        self.stdout.write(self.style.SUCCESS("Данные для Payment успешно добавлены!"))
