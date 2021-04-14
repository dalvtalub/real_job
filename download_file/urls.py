from django.urls import path
from .views import download_file

urlpatterns = [
    path('', download_file),
]