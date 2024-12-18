# Generated by Django 5.1.4 on 2024-12-18 08:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment_time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_time', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='time_slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeslote', models.CharField(max_length=50)),
                ('appointment_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='guest.appointment_time')),
            ],
        ),
    ]
