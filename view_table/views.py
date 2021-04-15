from django.shortcuts import render

from authentication.models import MyToken
from .models import *
from .forms import LibraryFilter
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
# from view_table.forms import AuthForm


def view_table(request):
    books = Books.objects.all()
    authors = Authors.objects.all()
    form = LibraryFilter(request.GET)
    if form.is_valid():
        if form.cleaned_data['author']:
            books = books.filter(author__name_and_surname__contains=form.cleaned_data['author'])
        if form.cleaned_data['year_of_book']:
            books = books.filter(year_of_writing__contains=form.cleaned_data['year_of_book'])
        if form.cleaned_data['name_of_book']:
            books = books.filter(name__contains=form.cleaned_data['name_of_book'])
        if form.cleaned_data['birth_year']:
            books = books.filter(author__date_of_birth__contains=form.cleaned_data['birth_year'])
    context = {
        'form': form,
        'authors': authors,
        'books': books,
    }
    return render(request, 'view_table.html', context)
