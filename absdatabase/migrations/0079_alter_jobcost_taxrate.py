# Generated by Django 3.2.13 on 2022-05-17 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0078_alter_taxrate_tax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobcost',
            name='taxrate',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=7, verbose_name=''),
        ),
    ]