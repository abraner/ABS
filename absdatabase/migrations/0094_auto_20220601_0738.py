# Generated by Django 3.2.13 on 2022-06-01 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0093_auto_20220531_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidpage',
            name='footinglaborcost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=7, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='bidpage',
            name='footingmatcost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=7, null=True, verbose_name=''),
        ),
    ]
