from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm

#
# class AuthForm(AuthenticationForm, ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')


class LibraryFilter(forms.Form):
    author = forms.CharField(label="Name or surname of author", required=False, max_length=40)
    birth_year = forms.IntegerField(label="Birth of author", required=False)
    year_of_book = forms.IntegerField(label="Year of book", required=False)
    name_of_book = forms.CharField(label="Name of author", required=False, max_length=40)
