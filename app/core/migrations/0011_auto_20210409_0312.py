# Generated by Django 3.1.7 on 2021-04-09 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_ingredient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='item',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='unit',
        ),
    ]