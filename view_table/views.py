from django.shortcuts import render
from .models import *
from .forms import LibraryFilter


def view_table(request):
    books = Books.objects.all()
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
    sort = ''
    if request.GET and "sort" in request.GET and request.GET['sort']:
        sort = request.GET['sort']
        books = books.order_by(sort)
    context = {
        'form': form,
        'books': books,
        'sort': sort,
    }
    return render(request, 'view_table.html', context)
