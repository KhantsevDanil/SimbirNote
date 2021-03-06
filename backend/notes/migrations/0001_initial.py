# Generated by Django 3.0.5 on 2022-03-09 13:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(help_text='what is the note about', max_length=15, verbose_name='about')),
                ('text', models.TextField(help_text='the main content of the post', verbose_name='Text')),
                ('date_create', models.DateTimeField(auto_now_add=True, help_text='Date note create', verbose_name='Date_create')),
                ('image', models.ImageField(blank=True, help_text='Upload image', null=True, upload_to='posts/', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('color', models.CharField(max_length=7, unique=True, validators=[django.core.validators.RegexValidator(message='Enter valid hex color number', regex='^#(?:[0-9a-fA-F]{3}){1,2}$')], verbose_name='Color')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Label')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
    ]
