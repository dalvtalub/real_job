import algorithm as algorithm
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import MyToken
from django.contrib.auth.models import User
import algorithm


def login(request):
    if request.POST:
        form = LoginForm(request.POST)
        name = form['name'].data
        password = form['password'].data
        if User.objects.filter(username=name).exists():
            user = User.objects.get(username=name)
            if user.check_password(password):
                return redirect('/')
            else:
                form = LoginForm()
                context = {
                    'form': form,
                    'invalid_data': 'Invalid name or password',
                }
                return render(request, 'login.html', context)
    else:
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)
