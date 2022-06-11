# Generated by Django 3.2.13 on 2022-05-11 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0022_alter_appqueue_apptime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bidpage',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False, verbose_name='ID.')),
                ('custid', models.IntegerField(default=None, null=True, verbose_name='Cust ID.')),
            ],
        ),
        migrations.AlterModelOptions(
            name='appqueue',
            options={'ordering': ['appdate', 'apptime']},
        ),
    ]
