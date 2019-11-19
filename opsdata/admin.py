from django.contrib import admin
from .models import Flight_Detail, Flight_Movement

# Register your models here.
admin.site.register(Flight_Detail)
admin.site.register(Flight_Movement)