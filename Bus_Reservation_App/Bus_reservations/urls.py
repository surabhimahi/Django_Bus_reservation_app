from .views import *
from django.urls import path

urlpatterns = [
    path('home/',home, name="home_page"),
    path('route/',route, name ="route_view"),
    path('location/',add_location, name ="location_view"),
    path('bus/',add_bus, name ="bus_view"),
    path('seat/',add_seat, name ="seat_view"),
    path('',login_view, name="login_view"),
    path('signup/',signup, name="signup_view"),
    path('logout/',logout_view, name="logout_view"),
    # path('route')
]