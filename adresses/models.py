from django.db import models


class Adress(models.Model):
    street_name = models.CharField()
    district = models.CharField()
    number = models.IntegerField()
    zip_code = models.CharField(max_length=8)
    city = models.CharField()
    state = models.CharField(max_length=2)
    address_complement = models.CharField()
    # Relation 1:1user
