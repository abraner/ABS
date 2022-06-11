# Generated by Django 3.2.13 on 2022-05-12 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0030_remove_bidpage_ceilingheight2'),
    ]

    operations = [
        migrations.CreateModel(
            name='heightft',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False, verbose_name='')),
                ('feet', models.CharField(blank=True, max_length=20, unique=True, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='heightin',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False, verbose_name='')),
                ('inches', models.CharField(blank=True, max_length=20, unique=True, verbose_name='')),
            ],
        ),
    ]