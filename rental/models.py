from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Film(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    image = models.ImageField(upload_to='films/', default='films/default.jpg')
    synopsis = models.TextField()  # Film description
    available = models.BooleanField(default=True)  # Availability status
    release_date = models.DateField()  # Release date

    def __str__(self):
        return self.title


class Rental(models.Model):
    film = models.ForeignKey('Film', on_delete=models.CASCADE)
    rental_date = models.DateField(default=timezone.now)  # Set default rental date to now
    return_date = models.DateField(null=True, blank=True)  # Allow return_date to be optional
    customer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.film.title} rented by {self.customer.username} on {self.rental_date}"
