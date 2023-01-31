from django.contrib import admin

from core.models import Location, Manufacturer, Car


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'country',
        'city',
        'street',
        'house_number',
    )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'manufacturer',
        'brand',
        'description',
        'year',
        'color',
        'type',
        'engine_power',
        'transmission',
        'price',
    )

