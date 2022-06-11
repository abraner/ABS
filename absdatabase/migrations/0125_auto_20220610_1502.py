# Generated by Django 3.2.13 on 2022-06-10 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absdatabase', '0124_alter_pdf_pdfs'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkType',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False, verbose_name='')),
                ('type', models.CharField(blank=True, max_length=20, unique=True, verbose_name='')),
            ],
        ),
        migrations.AddField(
            model_name='bidpage',
            name='worktype',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=''),
        ),
    ]