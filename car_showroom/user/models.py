from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models


class User(AbstractUser):

    email = models.EmailField(
        max_length=255,
        verbose_name="email",
        unique=True,
        null=False,
        blank=False
    )

    password = models.CharField(
        max_length=255,
        verbose_name="password",
        unique=True,
        null=False,
        blank=False
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]
