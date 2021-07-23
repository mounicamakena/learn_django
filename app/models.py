from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name


class Netflix(models.Model):
    show_id = models.CharField(max_length=100)
    show_type = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    cast = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date_added = models.CharField(max_length=100)
    release_year = models.IntegerField()
    rating = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    listed_in = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
