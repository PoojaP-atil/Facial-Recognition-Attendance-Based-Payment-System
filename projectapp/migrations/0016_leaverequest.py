# Generated by Django 4.2.7 on 2024-02-03 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0015_delete_leaverequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(max_length=2)),
                ('reason', models.CharField(max_length=500)),
                ('datefrom', models.DateField(max_length=200)),
                ('datetill', models.DateField(max_length=200)),
                ('is_approved', models.CharField(default='Unapproved', max_length=200)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.employee')),
            ],
        ),
    ]
