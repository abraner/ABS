# Generated by Django 3.2.13 on 2022-05-15 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0049_auto_20220515_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bidpage',
            name='beamlength2',
        ),
        migrations.RemoveField(
            model_name='bidpage',
            name='beamsize2',
        ),
    ]
