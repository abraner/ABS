# Generated by Django 3.2.13 on 2022-06-05 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0104_auto_20220605_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='finalpaydate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='termfinal',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='termfinal', to='absdatabase.downpayterms', verbose_name=''),
        ),
    ]
