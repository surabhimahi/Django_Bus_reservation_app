from django.db import models
# from django.db.models import 

# Create your models here.
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Route(models.Model):
    
    start_route =models.ForeignKey(Location,related_name='start', on_delete=models.CharField)
    end_route =models.ForeignKey(Location,related_name='end', on_delete=models.CharField)
    
    class Meta:
        unique_together = ('start_route', 'end_route')
        
    def __str__(self):
        return f'Start - {self.start_route} End - {self.end_route}'
    
class Seat(models.Model):
    SEAT_TYPE =[('seater', 'Seater'),
                ('sleeper', 'Sleeper')
                ]
    seat_no  = models.CharField(max_length=15, unique=True)
    seat_type =models.CharField(max_length=15,choices=SEAT_TYPE)
    seat_price = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return f'Seat No: {self.seat_no} Seat Type: {self.seat_type}  Seat Price: {self.seat_price}'

class Bus(models.Model):
    
    
    capacity = models.IntegerField()
    bus_no = models.CharField(max_length=20, unique=True)
    bus_name = models.CharField(max_length=20)
    SCHEDULE_CHOICES =[
        ('schedule_one', '00.00 - 06.00'),
        ('schedule_two', '07.00 - 12.00'),
        ('schedule_three', '13.00 - 18.00'),
        ('schedule_four', '19.00 - 24.00')
    ]
    
    schedule =models.CharField(max_length=50, choices=SCHEDULE_CHOICES, default=SCHEDULE_CHOICES[0])
    routes = models.ManyToManyField(Route, related_name='Buses', related_query_name="bus") 
    seats = models.ManyToManyField(Seat, related_name='Buses', related_query_name="bus") 
    
    
    def __str__(self):
        return f'Bus name {self.bus_name} Bus no  {self.bus_no}'   
    


    

    
  

    
    

     
    
        
    

    