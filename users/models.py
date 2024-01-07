from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    is_admin = models.BooleanField(default=False)
