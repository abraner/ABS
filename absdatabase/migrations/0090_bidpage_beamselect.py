# Generated by Django 3.2.13 on 2022-05-19 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0089_alter_bidpage_beamtype1'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidpage',
            name='beamselect',
            field=models.IntegerField(default=0.0, null=True, verbose_name=''),
        ),
    ]