from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .apps import UsersConfig
from .views import PaymentViewSet, UserProfileView, UsersCreateAPIView

router = DefaultRouter()
router.register(r'payments', PaymentViewSet)

app_name=UsersConfig.name

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UsersCreateAPIView.as_view(), name='register'),
    path('profile/<int:id>/', UserProfileView.as_view(), name='user-profile'),
    path('login/', TokenObtainPairView.as_view(), name='Login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]