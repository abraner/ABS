# Generated by Django 3.2.13 on 2022-05-17 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0081_auto_20220517_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobcost',
            name='totalmatcost',
        ),
    ]
