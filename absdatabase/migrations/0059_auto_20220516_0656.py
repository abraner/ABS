# Generated by Django 3.2.13 on 2022-05-16 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0058_auto_20220516_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidpage',
            name='miscqty1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='miscqty1', to='absdatabase.qty', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='bidpage',
            name='miscqty2',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='miscqty2', to='absdatabase.qty', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='bidpage',
            name='miscqty3',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='miscqty3', to='absdatabase.qty', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='bidpage',
            name='miscqty4',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='miscqty4', to='absdatabase.qty', verbose_name=''),
        ),
    ]
