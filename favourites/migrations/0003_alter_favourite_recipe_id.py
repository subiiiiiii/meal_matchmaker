# Generated by Django 4.2.5 on 2023-10-04 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favourites', '0002_alter_favourite_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourite',
            name='recipe_id',
            field=models.IntegerField(),
        ),
    ]
