from django.contrib import admin

# Register your models here.
from api.models import Cleaner, Customer, Appointment, City

admin.site.register(Cleaner)
admin.site.register(Customer)
admin.site.register(Appointment)
admin.site.register(City)
