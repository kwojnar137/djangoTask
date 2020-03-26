from django.db import models
from django.contrib.auth.models import AbstractUser
from random import random
from .validators import date_max


class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True, help_text='Maximum 20 characters')
    random_number = models.DecimalField(default=-1, decimal_places=0, max_digits=3)
    birth_date = models.DateField(null=False, blank=False, validators=[date_max], help_text='Required. Format: YYYY-MM-DD')
