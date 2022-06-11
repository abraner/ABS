# Generated by Django 3.2.13 on 2022-05-15 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0050_auto_20220515_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidpage',
            name='lclength2',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lclength2', to='absdatabase.qty', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='bidpage',
            name='lcqty2',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lcqty2', to='absdatabase.qty', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='bidpage',
            name='lctransition2',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lctransition2', to='absdatabase.lallycolumnreturn', verbose_name=''),
        ),
    ]
