# travel_app/models.py
from django.db import models

class TravelPreference(models.Model):
    destination = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    preferences = models.TextField()

    def __str__(self):
        return f"{self.destination} - {self.budget}"