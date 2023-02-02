from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_staffuser(self, email, username, password):
        user = self.create_user(
            email=email,
            password=password,
            username=username
        )

        user.staff = True
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )

        user.is_staff = True
        user.admin = True
        user.is_superuser = True

        user.save(using=self._db)

        return user
    
    
class User(AbstractUser):
    username = models.CharField(
        max_length=255,
        verbose_name="User's username",
        unique=True,
        null=False,
        blank=False,
    )

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

    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "password"]
