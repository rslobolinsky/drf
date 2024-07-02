from django.urls import path
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from users.apps import UsersConfig
from users.views import PaymentListAPIView, UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, \
    UserDestroyAPIView, PaymentCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('', UserListAPIView.as_view(), name='users_list'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='users_retrieve'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='users_update'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='users_delete'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
    path('payment/', PaymentListAPIView.as_view(), name='payment_list'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
]
