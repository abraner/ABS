# Generated by Django 3.2.13 on 2022-05-14 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0039_alter_bidpage_beamtype1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Beam',
        ),
        migrations.DeleteModel(
            name='GluLamBeam',
        ),
        migrations.DeleteModel(
            name='LVLBeam',
        ),
        migrations.DeleteModel(
            name='SteelBeam',
        ),
    ]
