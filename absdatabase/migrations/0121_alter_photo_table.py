# Generated by Django 3.2.13 on 2022-06-09 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0120_alter_photo_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='photo',
            table='jobphotos',
        ),
    ]