# Generated by Django 3.2.13 on 2022-05-15 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0051_auto_20220515_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bidpage',
            name='beamlength3',
        ),
        migrations.RemoveField(
            model_name='bidpage',
            name='beamsize3',
        ),
        migrations.RemoveField(
            model_name='bidpage',
            name='lclength3',
        ),
        migrations.RemoveField(
            model_name='bidpage',
            name='lcqty3',
        ),
        migrations.RemoveField(
            model_name='bidpage',
            name='lctransition3',
        ),
        migrations.RemoveField(
            model_name='bidpage',
            name='qty3',
        ),
    ]