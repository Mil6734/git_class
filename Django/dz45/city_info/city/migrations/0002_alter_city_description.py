# Generated by Django 4.2.5 on 2023-09-21 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='description',
            field=models.CharField(max_length=600),
        ),
    ]
