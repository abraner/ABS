# Generated by Django 3.2.13 on 2022-05-10 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0019_appointment_mainid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appqueuecount',
            name='id',
            field=models.AutoField(default=None, primary_key=True, serialize=False, verbose_name='ID.'),
        ),
    ]
