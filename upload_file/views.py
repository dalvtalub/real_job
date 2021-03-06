from django.shortcuts import render, redirect
from view_table.models import Books, Authors
from .forms import CsvForm
from .models import Csv

import csv


def upload_file(request):
    form = CsvForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        filename = (str(request.FILES['file_name'])).split('.')

        if not filename[-1] == 'csv':
            return render(request, 'upload_file.html',
                          {'form': CsvForm(), 'information': 'Invalid type of file, choose .csv file'})

        form.save()
        obj = Csv.objects.get(activated=False)
        print(obj.file_name.path)
        with open(obj.file_name.path) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            if len(header_row) != 4:
                return render(request, 'upload_file.html',
                              {'form': CsvForm(), 'information': 'File has incorrect data'})

            for row in reader:
                author_birth = int(row[0])
                author_name_and_surname = row[1]
                name_of_book = row[2]
                year_of_writing = int(row[3])
                if not Authors.objects.filter(date_of_birth=author_birth,
                                              name_and_surname=author_name_and_surname).exists():
                    Authors.objects.create(
                        date_of_birth=author_birth,
                        name_and_surname=author_name_and_surname,
                    )
                if not Books.objects.filter(year_of_writing=year_of_writing, name=name_of_book).exists():
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
        'information': 'Accepted only CSV files',
    }
    return render(request, 'upload_file.html', context)
