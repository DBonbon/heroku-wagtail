# Generated by Django 3.2.7 on 2021-10-10 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='about_subtitle',
        ),
    ]
