from django.db import models

from django.contrib.auth.models import User

class Authors(models.Model):
    """Model of Authors"""
    name_and_surname = models.CharField('Name and surname', max_length=40)
    date_of_birth = models.IntegerField('Year of birth')

    def __str__(self):
        return f'{self.name_and_surname}'

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Books(models.Model):
    """Model of Books"""
    year_of_writing = models.IntegerField('Year of writing')
    name = models.CharField('Name', max_length=40)
    # added ForeignKey. One to many, although one book can has more than one author
    author = models.ForeignKey(Authors, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
