from django.db import models
import uuid


class Address(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    street_name = models.CharField()
    district = models.CharField()
    number = models.IntegerField()
    zip_code = models.CharField(max_length=8)
    city = models.CharField()
    state = models.CharField(max_length=2)
    address_complement = models.CharField()
