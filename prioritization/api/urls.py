from django.contrib import admin
from django.urls import path, include
from .views import PrioritizationView, PrioritizationGetFile

urlpatterns = [
    path('priority',PrioritizationView.as_view()),
    path('get_priority',PrioritizationGetFile),
]