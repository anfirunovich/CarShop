from django.contrib.postgres.fields import DecimalRangeField
from django_countries.fields import CountryField

from core.model_mixins import CreatedAt, SoftDelete, UpdatedAt

from django.db import models

from customer.models import Customer
from supplier.models import Car, Supplier


class Location(CreatedAt, UpdatedAt, SoftDelete):

    country = CountryField(
        verbose_name="Location's country",
        null=False,
        blank=False
    )

    city = models.CharField(
        max_length=255,
        verbose_name="Location's city",
        null=False,
        blank=False
    )

    street = models.CharField(
        max_length=255,
        verbose_name="Street",
        null=False,
        blank=False
    )

    house_number = models.PositiveSmallIntegerField(
        verbose_name="House number",
        null=False,
        blank=False
    )

    def __str__(self):
        return f'{self.country}, {self.city}, {self.street}, {self.house_number}'


class Showroom(CreatedAt, SoftDelete, UpdatedAt):

    name = models.CharField(
        max_length=255,
        verbose_name="Name of showroom",
        unique=True,
        null=False,
        blank=False,
    )

    info = models.TextField(
        verbose_name="Info about showroom",
        null=True,
        blank=True,
    )

    locations = models.ManyToManyField(
        Location,
        verbose_name="Location of showroom",
        related_name="showrooms",
        related_query_name="showroom",
        blank=False,
    )

    balance = DecimalRangeField(
        verbose_name="Balance of showroom",
        null=True,
        min_value=0,
        max_value=9999999,
    )

    customers = models.ManyToManyField(
        Customer,
        related_name="showrooms",
        related_query_name="showroom",
    )

    cars = models.ManyToManyField(
        Car,
        related_name="showroom_cars",
        related_query_name="showroom_car",
    )

    def __str__(self):
        return self.name


class CarOfShowroom(CreatedAt, UpdatedAt, SoftDelete):

    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True,)
    showroom = models.ForeignKey(
        Showroom,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    count = models.PositiveIntegerField(default=1)


class ShowroomSale(CreatedAt, UpdatedAt, SoftDelete):

    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True,)
    showroom = models.ForeignKey(
        Showroom,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    discount = DecimalRangeField(
        max_digits=10,
        decimal_places=2,
        default=1,
        min_value=1,
        max_value=100,
    )

    end_date = models.DateField(blank=True)

