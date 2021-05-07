from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import *
from . import views
from django.urls import path

urlpatterns = [
    path('register' ,views.register, name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('get', Testting.as_view(), name='testting'),
    path('login', AuthView.as_view(), name='testting'),

    path('userlogin', views.userlogin, name='userlogin'),
    path('profile/<str:username>', views.profile, name='profile'),
]