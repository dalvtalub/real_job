import jwt

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User


from .forms import LoginForm
from .models import MyToken

import datetime as dt


def login(request):
    form = LoginForm()
    context = {
        'form': form,
    }
    if request.POST:
        form = LoginForm(request.POST)
        name = form['name'].data
        password = form['password'].data

        if not User.objects.filter(username=name).exists():
            context['invalid_data'] = 'Invalid name or password'
            return render(request, 'login.html', context)

        user = User.objects.get(username=name)

        if not user.check_password(password):
            context['invalid_data'] = 'Invalid name or password'
            return render(request, 'login.html', context)

        time = dt.datetime.now() + dt.timedelta(days=1)
        token = jwt.encode({
            'id': user.id,
            'exp': int(time.strftime('%S'))
        }, settings.SECRET_KEY, algorithm='HS256')
        if MyToken.objects.filter(user=user.id).exists():
            new_token = MyToken.objects.get(user=user.id)
            new_token.mytoken = token
            new_token.save()
        else:
            MyToken.objects.create(
                user=User.objects.get(username=name),
                mytoken=token,
            )
        response = redirect('/')
        response.set_cookie(
            "Auth_token",
            token,
        )
        return response
    else:

        if 'Auth_token' not in request.COOKIES:
            return render(request, 'login.html', context)
        token = request.COOKIES['Auth_token']

        if MyToken.objects.filter(mytoken=token).exists():
            return redirect('/')
        return render(request, 'login.html', context)


def logout(request):
    response = redirect('/')
    token = request.COOKIES['Auth_token']
    MyToken.objects.filter(mytoken=token).delete()
    response.delete_cookie('Auth_token')
    return response
