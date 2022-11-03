from django.db import models
import uuid

# Create your models here.

class Card(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    card_name = models.CharField(max_length=25)
    number_card = models.IntegerField(max_length=16)
    expire_date = models.CharField(max_length=6)
