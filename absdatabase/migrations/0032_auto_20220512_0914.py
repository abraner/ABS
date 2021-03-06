# Generated by Django 3.2.13 on 2022-05-12 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0031_heightft_heightin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidpage',
            name='beamtype1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beamtype1', to='absdatabase.beamtype', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='bidpage',
            name='chfeet1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chfeet1', to='absdatabase.heightft', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='bidpage',
            name='chinches1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chinches1', to='absdatabase.heightin', verbose_name=''),
        ),
    ]
