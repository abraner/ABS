# Generated by Django 3.2.13 on 2022-06-04 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0098_auto_20220602_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False, verbose_name='')),
                ('bidid', models.IntegerField(default=None, null=True, verbose_name='')),
                ('custid', models.IntegerField(default=None, null=True, verbose_name='')),
                ('grandtotalcost', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='')),
            ],
        ),
    ]
