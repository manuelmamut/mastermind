# Generated by Django 2.0.7 on 2018-07-06 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guesses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guess',
            name='guess_number',
        ),
    ]
