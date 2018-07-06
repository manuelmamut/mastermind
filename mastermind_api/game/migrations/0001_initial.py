# Generated by Django 2.0.7 on 2018-07-06 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('codemaker', models.CharField(max_length=100)),
                ('codebreaker', models.CharField(blank=True, max_length=100, null=True)),
                ('tries_number', models.IntegerField(choices=[(12, 'Easy'), (10, 'Medium'), (8, 'Hard'), (6, 'Pro')], default=12)),
                ('open_game', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
