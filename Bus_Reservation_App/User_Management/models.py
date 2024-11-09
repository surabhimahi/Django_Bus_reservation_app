from django.db import models

# Create your models here.

class Booking(models.Model):
    STATUS =[
        ('success', "Success"),
        ('cancelled', "Cancelled")
    ]
    
    booking_id =models.CharField(max_length=100, unique=True)
    booking_date =models.DateField()
    start_point = models.CharField(max_length=50)
    end_point = models.CharField(max_length=50)
    total_amount =models.DecimalField(decimal_places=2, max_digits=10)
    seat_no =models.CharField(max_length=100, default='L1')
    # passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE,  related_name='bookings')
    # seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name='bookings', d)
    booking_status =models.CharField(max_length=15, choices=STATUS, default='success')
    schedule =models.CharField(max_length=50, default='00.00 - 06.00')
    
    class Meta:
        unique_together = ('booking_date', 'start_point', 'end_point', 'seat_no','schedule')
    
    def __str__(self):
        return f'Booking ID: {self.booking_id} Booking Date : {self.booking_date} Passenger Name: {self.passenger} Total Amount {self.total_amount} Start point: {self.start_point} End point: {self.end_point}'


class Passenger(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number= models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    bookings = models.ManyToManyField(Booking, related_name='passengers')
    
    def __str__(self):
        return f'{self.name}'