# Generated by Django 5.1 on 2024-10-05 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bus_reservations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='bookings',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Passenger',
        ),
    ]
