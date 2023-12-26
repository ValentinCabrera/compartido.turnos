from django.urls import path
from .views import SheduleView

urlpatterns = [
    path("", SheduleView.as_view()),
]