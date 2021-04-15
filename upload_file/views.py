from django.http import HttpResponse
from django.shortcuts import render, redirect
from view_table.models import Books, Authors
from .forms import CsvForm
from .models import Csv

import csv


# from django.contrib.auth.decorators import login_required
#
#
# @login_required
def upload_file(request):
    form = CsvForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()  # after completing the addition - go to the galvanized page
        form = CsvForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            for row in reader:
                author_birth = int(row[0])
                author_name_and_surname = row[1]
                name_of_book = row[2]
                year_of_writing = int(row[3])
                if Authors.objects.filter(date_of_birth=author_birth, name_and_surname=author_name_and_surname).exists():
                    pass
                else:
                    Authors.objects.create(
                        date_of_birth=author_birth,
                        name_and_surname=author_name_and_surname,
                        )
                if Books.objects.filter(year_of_writing=year_of_writing, name=name_of_book).exists():
                    pass
                else:
                    Books.objects.create(
                        year_of_writing=year_of_writing,
                        name=name_of_book,
                        author=Authors.objects.get(name_and_surname=author_name_and_surname),
                    )
        obj.activated = True
        obj.save()
        return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'upload_file.html', context)
