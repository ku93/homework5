from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from materials.seriallizers import PaymentSerializer
from users.models import User


class UserSerializer(ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)
    password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'payments', 'password',]

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.is_active = True
        user.save()
