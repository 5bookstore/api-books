from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    cpf = models.CharField(max_length=14, unique=True)

    address = models.OneToOneField(
        "addresses.Address",
        related_name="user",
        on_delete=models.CASCADE,
    )

    card = models.OneToOneField(
        "cards.Card",
        related_name="user",
        on_delete=models.CASCADE,
    )
