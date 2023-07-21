from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class password(models.Model):
    hashed_password = models.CharField(max_length=200, default="hello")
    title = models.CharField(max_length=32)
    website = models.CharField(max_length=32)
    notes = models.CharField(max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="according_passwords")

    def __str__(self):
        return f"{self.title} password by {self.owner}"
