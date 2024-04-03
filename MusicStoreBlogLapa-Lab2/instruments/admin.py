from django.contrib import admin

# Register your models here.
from .models import Instrument, Order
admin.site.register(Instrument)
admin.site.register(Order)