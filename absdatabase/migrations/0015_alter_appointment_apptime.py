# Generated by Django 3.2.13 on 2022-05-09 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0014_alter_appointment_apptime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='apptime',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name=''),
        ),
    ]
