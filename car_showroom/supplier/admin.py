from django.contrib import admin

from supplier.models import Supplier, CarOfSupplier, SupplierSale


@admin.register(Supplier)
class SupplierModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'info',
        'foundation_date',
    )


@admin.register(CarOfSupplier)
class CarOfSupplierModelAdmin(admin.ModelAdmin):
    list_display = (
        'supplier',
        'count',
    )


@admin.register(SupplierSale)
class SupplierSaleModelAdmin(admin.ModelAdmin):
    list_display = (
        'supplier',
        'discount',
        'end_date',
    )
