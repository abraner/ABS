# Generated by Django 3.2.13 on 2022-05-17 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0082_remove_jobcost_totalmatcost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobcost',
            name='prodqueue',
        ),
    ]