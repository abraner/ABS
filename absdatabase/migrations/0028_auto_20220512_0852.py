# Generated by Django 3.2.13 on 2022-05-12 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0027_alter_bidpage_beamtype1'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidpage',
            name='chfeet1',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='bidpage',
            name='chinches1',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name=''),
        ),
    ]
