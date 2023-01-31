from django.contrib import admin

from showroom.models import Showroom, CarOfShowroom, ShowroomSale


@admin.register(Showroom)
class ShowroomModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'info',
    )


@admin.register(CarOfShowroom)
class CarOfShowroomModelAdmin(admin.ModelAdmin):
    list_display = (
        'showroom',
        'supplier',
        'count',
    )


@admin.register(ShowroomSale)
class ShowroomSaleModelAdmin(admin.ModelAdmin):
    list_display = (
        'showroom',
        'discount',
        'end_date',
    )