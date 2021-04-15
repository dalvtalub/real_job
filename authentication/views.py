from django.shortcuts import render
from .models import MyToken
from django.contrib.auth.models import User


def login(request):
    if request.POST:

    return render(request, 'login.html')
