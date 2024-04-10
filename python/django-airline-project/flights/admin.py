from django.contrib import admin
from .models import Airport, Flight, Passenger


# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Flight._meta.fields]


class AirportAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Airport._meta.fields]


class PassengerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Passenger._meta.fields]
    filter_horizontal = ("flights",)


admin.site.register(Airport, AirportAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
