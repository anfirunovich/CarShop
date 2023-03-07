from django.conf import settings
from django.db import models

from core.model_mixins import CreatedAt, SoftDelete, UpdatedAt
from core.validators import phone_number_validator

from customer.enums.person_sexes import PersonSexesEnum

from core.models import Car


class Customer(CreatedAt, SoftDelete, UpdatedAt):

    first_name = models.CharField(
        max_length=255,
        verbose_name=" First name",
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=255,
        verbose_name="Last name",
        null=False,
        blank=False,
    )

    sex = models.CharField(
        max_length=255,
        verbose_name="Sex",
        choices=PersonSexesEnum.choices(),
        blank=True,
        null=True,
    )

    phone_number = models.CharField(
        max_length=20,
        verbose_name="Phone number",
        blank=True,
        null=True,
        validators=(phone_number_validator,),
    )

    balance = models.DecimalField(max_digits=10, decimal_places=2)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Offer(CreatedAt, SoftDelete, UpdatedAt):

    requested_car_manufacturer = models.CharField(
        max_length=20,
        verbose_name="Manufacturer requested by customer",
        blank=True,
        null=True,
    )

    requested_car_brand = models.CharField(
        max_length=20,
        verbose_name="Brand requested by customer",
        blank=True,
        null=True,
    )

    requested_car_color = models.CharField(
        max_length=20,
        verbose_name="Color requested by customer",
        blank=True,
        null=True,
    )

    requested_car_type = models.CharField(
        max_length=20,
        verbose_name="Type requested by customer",
        blank=True,
        null=True,
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    max_price = models.DecimalField(max_digits=10, decimal_places=2)


class PurchaseHistory(CreatedAt, SoftDelete, UpdatedAt):

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    offer = models.ForeignKey(
        Offer,
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

    showroom = models.ForeignKey(
        "showroom.Showroom",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    total_price = models.DecimalField(max_digits=10, decimal_places=2)
