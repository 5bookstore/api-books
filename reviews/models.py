from django.db import models
import uuid

# Create your models here.

class Review(models.Model):
    stars = models.PositiveIntegerField(min_length = 1, max_length = 5)
    rating = models.CharField(max_length = 600)
