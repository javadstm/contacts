# Generated by Django 3.2.9 on 2021-11-24 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0010_auto_20211123_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(blank=True, default='none', max_length=48),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(blank=True, default='none', max_length=64),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(blank=True, default='none', max_length=20, unique=True),
        ),
    ]
