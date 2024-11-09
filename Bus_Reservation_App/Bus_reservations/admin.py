from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Bus)
admin.site.register(Seat)
admin.site.register(Route)
# admin.site.register(Schedule)