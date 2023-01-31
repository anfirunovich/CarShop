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
        'customer',
        'car',
        'max_price',
    )
