import django_filters
from .models import Payment


class PaymentFilter(django_filters.FilterSet):
    course = django_filters.NumberFilter(field_name='course__id')
    lesson = django_filters.NumberFilter(field_name='lesson__id')
    payment_method = django_filters.CharFilter(field_name='payment_method')
    payment_date = django_filters.DateFilter(field_name='payment_date__date')

    class Meta:
        model = Payment
        fields = ['course', 'lesson', 'payment_method', 'payment_date']
