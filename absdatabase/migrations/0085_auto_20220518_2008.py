# Generated by Django 3.2.13 on 2022-05-19 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0084_bidpage_prodqueue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidpage',
            name='beamsize1',
            field=models.IntegerField(default=None, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='bidpage',
            name='beamtype1',
            field=models.IntegerField(default=None, null=True, verbose_name=''),
        ),
    ]
