from django.shortcuts import redirect, render
import json
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from .myforms import *
from django.contrib.auth.models import User
from django.contrib import messages
# from models import user

# sampple text
# Create your views here.

def home(request):
    return render (request, 'bus_reservations/home.html')


def add_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('location_view')  
    else:
        form = LocationForm()

    locations = Location.objects.all()
    return render(request, 'bus_reservations/add_location.html', {'form': form, 'locations': locations})


def add_bus(request):
    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bus_view')  
    else:
        form = BusForm()

    bus = Bus.objects.all()
    routes = bus.routes.all();
    return render(request, 'bus_reservations/add_bus.html', {'form': form, 'bus': bus})

def add_seat(request):
    if request.method == 'POST':
        form = SeatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seat_view')  
    else:
        form = SeatForm()

    seat = Seat.objects.all()
    return render(request, 'bus_reservations/add_seat.html', {'form': form, 'seats': seat})
 


def route(request):
    
    if request.method =='POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            start = form.cleaned_data['start_route']
            end = form.cleaned_data['end_route']
            if start != end :
                form.save() 
                messages.error(request, message=f"{start } route to {end } route added successfully ")
            else:
                messages.error(request, message="Start and End route should be different")
    else:
        form = RouteForm()  
    return render (request, 'bus_reservations/route.html', {'form':form})
        # try:
        #     route_data =json.loads(request.body)
        #     start_point =route_data.get('start_point')
        #     end_point =route_data.get('end_point')
        #     if start_point and end_point:
        #         if start_point== end_point:
        #             return JsonResponse({'error': 'Both fields should not be same'})
        #         else:
        #             new_route = Route.objects.create(start_route=start_point, end_route=end_point)
        #             new_route.save()
        #             return JsonResponse({'message':'New route created successfully'})
                    
            
        # except json.JSONDecodeError:
        #     return JsonResponse({'error': 'Invalid JSON'}, status=400)
            
    # elif request.method =='GET':
    #     routes = Route.objects.all()
    #     routes_list = list(routes.values('start_route', 'end_route'))
    #     return JsonResponse({'routes':routes_list})
        
    # else:
    #     return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
        
        
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            if User.objects.filter(username=username).exists():
              
                user = authenticate(request, username=username, password=password)
                if user is not None:
         
                    login(request, user)
                    return redirect('home_page')  
                else: 
                    print("yess")
                    messages.error(request, 'Enter correct username and password.')
            else: 
                messages.error(request, 'Username not found. Kindly sign up.')
    else:
        form = LoginForm() 

    return render(request, 'bus_reservations/login.html', {'form': form})


def signup(request):
    
    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user =form.save()
            user.is_superuser = True  # Set as superuser
            user.is_staff = True  # Required for admin access
            user.save()
            return redirect('login_view')
    else:
        form = SignupForm()
        
    return render(request, 'bus_reservations/signup.html' , {'form':form})

def logout_view(request):
    logout(request)
    return redirect('login_view')