# Generated by Django 3.2.13 on 2022-05-05 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0006_alter_customerinfo_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerinfo',
            name='prodqueue',
        ),
    ]