from .models import *
from django import forms


class CsvForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ('file_name',)