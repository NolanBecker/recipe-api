# Generated by Django 3.1.7 on 2021-04-09 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210409_0344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='items',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='core.Ingredient'),
        ),
    ]
