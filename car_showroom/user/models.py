from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):

    email = models.EmailField(
        max_length=255,
        verbose_name="email",
        unique=True,
        null=False,
        blank=False
    )

    password = models.CharField(
        max_length=8,
        verbose_name="password",
        unique=True,
        null=False,
        blank=False
    )

    USERNAME_FIELD = "email"
