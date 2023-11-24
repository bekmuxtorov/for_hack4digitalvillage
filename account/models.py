from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from rest_framework.authtoken.models import Token
from .managers import UserManager


class TokenProxy(Token):
    class Meta:
        proxy = True
        verbose_name = "Token"
        verbose_name_plural = "Tokens"


class Account(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(
        verbose_name="phone number",
        max_length=20,
        unique=True,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^\+998\d{9}$',
                message='Invalid phone number. Please enter in the format +998901234567'
            )
        ]
    )
    full_name = models.CharField(
        verbose_name="Full name",
        max_length=100,
    )
    farm_name = models.CharField(
        verbose_name="Farm name",
        max_length=50,
        blank=True
    )
    is_staff = models.BooleanField(
        verbose_name="is staff",
        default=False
    )
    created_at = models.DateTimeField(
        verbose_name="Date of creation",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="update profile",
        auto_now=True,
        blank=True,
        null=True
    )

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def __str__(self):
        return self.full_name
