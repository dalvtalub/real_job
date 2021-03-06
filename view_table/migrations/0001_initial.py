# Generated by Django 3.1.8 on 2021-04-15 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_and_surname', models.CharField(max_length=40, verbose_name='Name and surname')),
                ('date_of_birth', models.IntegerField(verbose_name='Year of birth')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_writing', models.IntegerField(verbose_name='Year of writing')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='view_table.authors')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]
