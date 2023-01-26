from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import DecimalRangeField

from core.model_mixins import CreatedAt, SoftDelete, UpdatedAt

from supplier.enums.car_color import CarColor
from supplier.enums.car_transmission import TransmissionType
from supplier.enums.car_type import CarType

from django.db import models
from showroom.models import Showroom
from showroom.models import Location


class Car(CreatedAt, UpdatedAt, SoftDelete):

    manufacturer = models.CharField(
        max_length=255,
        verbose_name="Сar manufacturer",
        null=False,
        blank=False,
    )

    brand = models.CharField(
        max_length=255,
        verbose_name="Brand of car",
        null=False,
        blank=False,
    )

    description = models.TextField(verbose_name="Description of car", null=True, blank=True,)

    year = models.IntegerField(
        validators=(
            MaxValueValidator(2023),
            MinValueValidator(1999),
        )
    )

    color = models.CharField(
        max_length=255,
        verbose_name="Color of car",
        blank=True,
        choices=CarColor.choices(),
    )

    type = models.CharField(
        max_length=255,
        verbose_name="Type of car",
        blank=True,
        choices=CarType.choices(),
    )

    engine_power = models.PositiveSmallIntegerField(
        validators=(
            MaxValueValidator(900),
            MinValueValidator(100),
        )
    )

    transmission = models.CharField(
        max_length=255,
        verbose_name="Transmission",
        blank=True,
        choices=TransmissionType.choices(),
    )

    price = DecimalRangeField(null=True, min_value=1, max_value=9999999,)

    def __str__(self):
        return self.name


class Supplier(CreatedAt, UpdatedAt, SoftDelete):

    name = models.CharField(
        max_length=255,
        verbose_name="Name of supplier",
        unique=True,
        null=False,
        blank=False,
    )

    info = models.TextField(verbose_name="Info about supplier", null=True, blank=True,)
    foundation_date = models.DateField(verbose_name="Foundation date", null=True, blank=True)

    locations = models.ManyToManyField(
        Location,
        verbose_name="Location of supplier",
        related_name="supplier",
        related_query_name="supplier",
        blank=False,
    )

    cars = models.ManyToManyField(Car)

    customers = models.ManyToManyField(
        Showroom,
        related_name="suppliers",
        related_query_name="supplier",
    )

    def __str__(self):
        return self.name


class CarOfSupplier(CreatedAt, UpdatedAt, SoftDelete):

    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True,)
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    count = models.PositiveIntegerField(default=1)


class SupplierSale(CreatedAt, UpdatedAt, SoftDelete):

    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, )
    supplier = models.ForeignKey(
        Supplier,
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

