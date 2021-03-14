from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    email = models.CharField(max_length=250,null=False, blank=False, unique=True)
    password = models.CharField(max_length=250, null=False, blank=False)
    username = models.CharField(max_length=250, null=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']





