from django.urls import path

from .views import index

urlpatterns = [
    path('', index),
    path('admin/dashboard', index),
    path('admin', index),
    path('rtl', index)
]