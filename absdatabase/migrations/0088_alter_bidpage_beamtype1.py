# Generated by Django 3.2.13 on 2022-05-19 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0087_beamtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidpage',
            name='beamtype1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beamtype1', to='absdatabase.beamtype', verbose_name=''),
        ),
    ]
