from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    patronymic = models.CharField(max_length=30, blank=True)
