# Generated by Django 4.2.7 on 2024-01-22 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0004_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='in_time',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='out_time',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(default='', max_length=100),
        ),
    ]
