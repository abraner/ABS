# Generated by Django 3.2.13 on 2022-05-17 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0083_remove_jobcost_prodqueue'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidpage',
            name='prodqueue',
            field=models.ForeignKey(blank=True, default=0.0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prodqueue', to='absdatabase.prodqueue', to_field='increase', verbose_name=''),
        ),
    ]
