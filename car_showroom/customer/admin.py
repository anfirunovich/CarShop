from django.contrib import admin

from customer.models import Customer, Offer


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'sex',
        'phone_number',
        'balance',
        'user',
    )


@admin.register(Offer)
class OfferModelAdmin(admin.ModelAdmin):
    list_display = (
        'requested_car_manufacturer',
        'requested_car_brand',
        'requested_car_color',
        'requested_car_type',
        'customer',
        'max_price',
    )


