# Generated by Django 3.2.13 on 2022-06-11 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0132_auto_20220611_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidpage',
            name='beamlength1ft',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beamlength1ft', to='absdatabase.beamft', to_field='feet', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='bidpage',
            name='beamlength1in',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beamlength1in', to='absdatabase.heightin', to_field='inches', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='bidpage',
            name='lclength1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lclength1', to='absdatabase.qty', to_field='quantity', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='bidpage',
            name='lcqty1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lcqty1', to='absdatabase.qty', to_field='quantity', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='bidpage',
            name='lctransition1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lctransition1', to='absdatabase.lallycolumnreturn', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='bidpage',
            name='qty1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='row1qty', to='absdatabase.qty', to_field='quantity', verbose_name=''),
        ),
    ]