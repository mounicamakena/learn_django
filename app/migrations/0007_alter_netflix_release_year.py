# Generated by Django 3.2.5 on 2021-07-23 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_netflix_release_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='netflix',
            name='release_year',
            field=models.IntegerField(),
        ),
    ]