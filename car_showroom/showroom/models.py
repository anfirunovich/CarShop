from django.contrib.postgres.fields import DecimalRangeField
from django.db import models

from core.model_mixins import CreatedAt, SoftDelete, UpdatedAt
from core.models import Location, Car

from customer.models import Customer


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

    balance = models.DecimalField(
        verbose_name="Balance of showroom",
        max_digits=10,
        decimal_places=2,
        null=True
    )

    customers = models.ManyToManyField(
        Customer,
        verbose_name="Customer",
        related_name="showrooms",
        related_query_name="showroom",
    )

    cars = models.ManyToManyField(
      Car,
      verbose_name="Car",
      through="CarOfShowroom",
      through_fields=('showroom', 'car'),
      related_name="showroom_cars",
      related_query_name="showroom_car",
    )

    def __str__(self):
        return self.name


class CarOfShowroom(CreatedAt, UpdatedAt, SoftDelete):

    car = models.ForeignKey(
        Car,
        verbose_name="Car",
        on_delete=models.SET_NULL,
        null=True,
    )

    showroom = models.ForeignKey(
        Showroom,
        verbose_name="Showroom",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    supplier = models.ForeignKey(
       "supplier.Supplier",
       verbose_name="Supplier",
       on_delete=models.CASCADE,
       null=True,
       blank=True,
    )

    price = models.DecimalField(max_digits=5, decimal_places=1)

    count = models.PositiveIntegerField(default=1)


class ShowroomSale(CreatedAt, UpdatedAt, SoftDelete):

    car = models.ForeignKey(
        Car,
        verbose_name="Showroom sale",
        on_delete=models.SET_NULL,
        null=True
    )

    showroom = models.ForeignKey(
       Showroom,
       verbose_name="Showroom",
       on_delete=models.CASCADE,
       null=True,
       blank=True,
    )

    discount = DecimalRangeField(default=1)
    end_date = models.DateField(blank=True)

