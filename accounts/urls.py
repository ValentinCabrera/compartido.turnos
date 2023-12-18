from django.urls import path
from .views import LogInView, SignInView

urlpatterns = [
    path("login/", LogInView.as_view()),
    path("signin/", SignInView.as_view()),
]