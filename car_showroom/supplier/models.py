from django.contrib.postgres.fields import DecimalRangeField
from django.db import models

from core.model_mixins import CreatedAt, SoftDelete, UpdatedAt
from core.models import Car, Location

from showroom.models import Showroom


class Supplier(CreatedAt, UpdatedAt, SoftDelete):

    name = models.CharField(
        max_length=255,
        verbose_name="Name of supplier",
        unique=True,
        null=False,
        blank=False,
    )

    info = models.TextField(verbose_name="Info about supplier", null=True, blank=True)
    foundation_date = models.DateField(verbose_name="Foundation date", null=True, blank=True)

    locations = models.ManyToManyField(
        Location,
        verbose_name="Location of supplier",
        related_name="suppliers",
        related_query_name="supplier",
        blank=False,
    )

    cars = models.ManyToManyField(
        Car,
        verbose_name="Car of supplier",
        through="CarOfSupplier",
        through_fields=('supplier', 'car'),
        related_name="suppliers",
        related_query_name="supplier",
    )

    customers = models.ManyToManyField(
        Showroom,
        verbose_name="Customer of supplier",
        related_name="suppliers",
        related_query_name="supplier",
    )

    def __str__(self):
        return self.name


class CarOfSupplier(CreatedAt, UpdatedAt, SoftDelete):

    car = models.ForeignKey(
        Car,
        verbose_name="Car",
        related_name="cars_of_suppliers",
        related_query_name="car_of_supplier",
        on_delete=models.SET_NULL,
        null=True,
    )

    supplier = models.ForeignKey(
        Supplier,
        verbose_name="Supplier",
        related_name="cars_of_suppliers",
        related_query_name="car_of_supplier",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    price = models.DecimalField(max_digits=5, decimal_places=1)

    count = models.PositiveIntegerField(verbose_name="Count of car", default=1)


class SupplierSale(CreatedAt, UpdatedAt, SoftDelete):

    car = models.ForeignKey(
        Car,
        verbose_name="Car",
        on_delete=models.SET_NULL,
        null=True
    )

    supplier = models.ForeignKey(
        Supplier,
        verbose_name="Supplier",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    discount = DecimalRangeField(default=1)
    end_date = models.DateField(blank=True)

