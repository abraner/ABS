# Generated by Django 3.2.13 on 2022-06-06 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0109_auto_20220605_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Percentage',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False, verbose_name='')),
                ('percent', models.CharField(blank=True, max_length=50, verbose_name='')),
                ('multiplier', models.DecimalField(decimal_places=2, default='0.00', max_digits=7, unique=True, verbose_name='')),
            ],
        ),
    ]
