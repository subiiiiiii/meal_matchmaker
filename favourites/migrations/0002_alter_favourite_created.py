# Generated by Django 4.2.5 on 2023-10-04 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favourites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourite',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]