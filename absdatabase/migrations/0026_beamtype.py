# Generated by Django 3.2.13 on 2022-05-12 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0025_auto_20220512_0739'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeamType',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False, verbose_name='')),
                ('beam_type', models.CharField(blank=True, max_length=20, unique=True, verbose_name='')),
            ],
        ),
    ]
