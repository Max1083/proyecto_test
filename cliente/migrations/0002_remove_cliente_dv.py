# Generated by Django 3.0.5 on 2021-08-17 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='dv',
        ),
    ]