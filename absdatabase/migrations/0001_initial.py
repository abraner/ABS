# Generated by Django 3.2.13 on 2022-05-03 17:51

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProdQueue',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False, verbose_name='ID.')),
                ('production', models.CharField(blank=True, max_length=50, unique=True, verbose_name='Production')),
                ('increase', models.DecimalField(decimal_places=2, default='0.00', max_digits=7, unique=True, verbose_name='Increase / Decrease')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerInfo',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False, verbose_name='ID.')),
                ('custid', models.IntegerField(default=None, null=True, verbose_name='Cust ID.')),
                ('conid', models.IntegerField(default=None, null=True, verbose_name='Con. ID.')),
                ('custcompanytname', models.CharField(blank=True, max_length=50, verbose_name='Company Name:')),
                ('custfirstname', models.CharField(max_length=45, verbose_name='First Name:')),
                ('custlastname', models.CharField(max_length=45, verbose_name='Last Name:')),
                ('custadd1', models.CharField(max_length=45, verbose_name='Address #1:')),
                ('custadd2', models.CharField(blank=True, max_length=45, verbose_name='Address #2:')),
                ('custcity', models.CharField(max_length=45, verbose_name='City:')),
                ('custst', models.CharField(max_length=2, verbose_name='St:')),
                ('custzipcode', models.CharField(max_length=15, verbose_name='Zip Code:')),
                ('custwork1', phone_field.models.PhoneField(blank=True, max_length=31, verbose_name='Work Phone #1:')),
                ('custwork2', phone_field.models.PhoneField(blank=True, max_length=31, verbose_name='Work Phone #2:')),
                ('custcell1', phone_field.models.PhoneField(blank=True, max_length=31, verbose_name='Cell Phone #1:')),
                ('custcell2', phone_field.models.PhoneField(blank=True, max_length=31, verbose_name='Cell Phone #2:')),
                ('custhome', phone_field.models.PhoneField(blank=True, max_length=31, verbose_name='Home Phone:')),
                ('custemail1', models.EmailField(blank=True, max_length=254, verbose_name='Email #1:')),
                ('custemail2', models.EmailField(blank=True, max_length=254, verbose_name='Email #2:')),
                ('prodqueue', models.ForeignKey(blank=True, default='0.00', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prodqueue', to='absdatabase.prodqueue', to_field='increase', verbose_name='')),
            ],
        ),
    ]
