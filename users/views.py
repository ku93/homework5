from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet

from materials.seriallizers import PaymentSerializer
from users.filters import PaymentFilter
from users.models import Payment, User
from users.seriallizers import UserSerializer


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PaymentFilter
    ordering_fields = ['payment_date']

class UserProfileView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

class UsersCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

