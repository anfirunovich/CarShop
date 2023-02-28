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
        'Showroom',
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
       'Showroom',
       verbose_name="Showroom",
       on_delete=models.CASCADE,
       null=True,
       blank=True,
    )

    discount = DecimalRangeField(default=1)
    end_date = models.DateField(blank=True)


class ShowroomOffer(CreatedAt, SoftDelete, UpdatedAt):

    requested_car_manufacturer = models.CharField(
        max_length=20,
        verbose_name="Manufacturer requested by showroom",
        blank=True,
        null=True,
    )

    requested_car_brand = models.CharField(
        max_length=20,
        verbose_name="Brand requested by showroom",
        blank=True,
        null=True,
    )

    requested_car_color = models.CharField(
        max_length=20,
        verbose_name="Color requested by showroom",
        blank=True,
        null=True,
    )

    requested_car_type = models.CharField(
        max_length=20,
        verbose_name="Type requested by showroom",
        blank=True,
        null=True,
    )

    showroom = models.ForeignKey('Showroom', on_delete=models.CASCADE)
    max_price = models.DecimalField(max_digits=10, decimal_places=2)


class ShowroomPurchaseHistory(CreatedAt, SoftDelete, UpdatedAt):

    showroom = models.ForeignKey(
        "showroom.Showroom",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    offer = models.ForeignKey(
        ShowroomOffer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    car = models.ForeignKey(
        Car,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    supplier = models.ForeignKey(
        "supplier.Supplier",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    total_price = models.DecimalField(max_digits=10, decimal_places=2)
