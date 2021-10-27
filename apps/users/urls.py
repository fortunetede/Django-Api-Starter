
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter
from apps.users.views import UserSignUp, UserLogin

urlpatterns = [
    path('user/signup/', UserSignUp.as_view()),
    path('user/login/', UserLogin.as_view()),
]
