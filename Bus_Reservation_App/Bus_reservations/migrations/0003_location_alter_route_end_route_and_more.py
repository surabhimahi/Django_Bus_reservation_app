# Generated by Django 5.1 on 2024-10-07 04:48

import django.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bus_reservations', '0002_remove_passenger_bookings_delete_booking_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='route',
            name='end_route',
            field=models.ForeignKey(on_delete=django.db.models.fields.CharField, related_name='end', to='Bus_reservations.location'),
        ),
        migrations.AlterField(
            model_name='route',
            name='start_route',
            field=models.ForeignKey(on_delete=django.db.models.fields.CharField, related_name='start', to='Bus_reservations.location'),
        ),
    ]