# Generated by Django 3.2.13 on 2022-05-16 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0054_alter_bidpage_footingqty'),
    ]

    operations = [
        migrations.CreateModel(
            name='FootingSize',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False, verbose_name='')),
                ('footingdim', models.CharField(blank=True, max_length=20, verbose_name='')),
            ],
        ),
    ]