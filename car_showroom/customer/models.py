from core.model_mixins import CreatedAt, SoftDelete, UpdatedAt
from core.validators import phone_number_validator

from customer.enums.person_sexes import PersonSexesEnum

from django.db import models
from supplier.models import Car


class Customer(CreatedAt, SoftDelete, UpdatedAt):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    sex = models.CharField(
        max_length=255,
        choices=PersonSexesEnum.choices(),
        blank=True,
        null=True
    )

    phone_number = models.CharField(
        max_length=20,
        verbose_name="Phone number",
        blank=True,
        null=True,
        validators=(phone_number_validator,),
    )

    balance = models.DecimalField(min_value=0, max_value=9999999,)


class Offer(CreatedAt, SoftDelete, UpdatedAt):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    max_price = models.DecimalField(null=True, min_value=1, max_value=9999999,)



