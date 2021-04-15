from django.http import HttpResponse

import jwt

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User

from .forms import LoginForm
from .models import MyToken

import datetime as dt


def set_cookies_function(request, token):
    response = HttpResponse('')
    response.set_cookie("Auth_token", token,  365 * 24 * 60 * 60,)
    return response


def login(request):
    if request.POST:
        form = LoginForm(request.POST)
        name = form['name'].data
        password = form['password'].data
        if User.objects.filter(username=name).exists():
            user = User.objects.get(username=name)
            if user.check_password(password):
                time = dt.datetime.now() + dt.timedelta(days=1)
                token = jwt.encode({
                    'id': user.id,
                    'exp': int(time.strftime('%S'))
                }, settings.SECRET_KEY, algorithm='HS256')
                if MyToken.objects.filter(user=user.id).exists():
                    new_token = MyToken.objects.get(user=user.id)
                    new_token.mytoken = token
                    new_token.save()
                    set_cookies_function(request, new_token)
                else:
                    MyToken.objects.create(
                        user=User.objects.get(username=name),
                        mytoken=token,
                    )
                    set_cookies_function(request, token)
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