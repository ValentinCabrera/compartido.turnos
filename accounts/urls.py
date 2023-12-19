from django.urls import path
from .views import LogInView, SignInView, CheckMailView

urlpatterns = [
    path("login/", LogInView.as_view()),
    path("signin/", SignInView.as_view()),
    path("check-mail/", CheckMailView.as_view())
]