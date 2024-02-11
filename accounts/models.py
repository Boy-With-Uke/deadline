from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nom = models.CharField(max_length=128)
    prenom = models.CharField(max_length=128)
    localisation = models.CharField(max_length=120)
    cin = models.IntegerField()
    password = models.CharField(max_length=128)
    surete = models.IntegerField(default=0)
