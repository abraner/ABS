# Generated by Django 3.2.13 on 2022-05-06 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0010_alter_customerinfo_custcompanytname'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.DateField(auto_now=True, null=True, verbose_name=''),
        ),
    ]
