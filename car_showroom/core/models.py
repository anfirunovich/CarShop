from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import DecimalRangeField
from django.db import models

from django_countries.fields import CountryField

from core.model_mixins import CreatedAt, SoftDelete, UpdatedAt
from core.enums.car_transmission import TransmissionType
from core.enums.car_color import CarColor
from core.enums.car_type import CarType


class Location(CreatedAt, UpdatedAt, SoftDelete):

    country = CountryField(
        verbose_name="Location's country",
        null=False,
        blank=False,
    )

    city = models.CharField(
        max_length=255,
        verbose_name="Location's city",
        null=False,
        blank=False,
    )

    street = models.CharField(
        max_length=255,
        verbose_name="Street",
        null=False,
        blank=False,
    )

    house_number = models.PositiveSmallIntegerField(
        verbose_name="House number",
        null=False,
        blank=False,
    )

    def __str__(self):
        return f'{self.country}, {self.city}, {self.street}, {self.house_number}'


class Manufacturer(CreatedAt, UpdatedAt, SoftDelete):

    name = models.CharField(
        max_length=255,
        verbose_name="Name of manufacturer",
        unique=True,
        null=False,
        blank=False,
    )

    description = models.TextField(verbose_name="Description of manufacturer", null=True, blank=True)

    locations = models.ManyToManyField(
        Location,
        verbose_name="Location of manufacturer",
        related_name="manufacturers",
        related_query_name="manufacturer",
        blank=False,
    )


class Car(CreatedAt, UpdatedAt, SoftDelete):

    manufacturer = models.ForeignKey(
        Manufacturer,
        max_length=255,
        verbose_name="Сar manufacturer",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    brand = models.CharField(
        max_length=255,
        verbose_name="Brand of car",
        null=False,
        blank=False,
    )

    description = models.TextField(verbose_name="Description of car", null=True, blank=True)

    year = models.IntegerField(
        validators=(
            MaxValueValidator(2023),
            MinValueValidator(1999),
        )
    )

    color = models.CharField(
        max_length=6,
        verbose_name="Color of car",
        blank=True,
        choices=CarColor.choices(),
    )

    type = models.CharField(
        max_length=11,
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
        max_length=9,
        verbose_name="Transmission",
        blank=True,
        choices=TransmissionType.choices(),
    )

    def __str__(self):
        return f"{self.manufacturer.name} {self.brand}"

