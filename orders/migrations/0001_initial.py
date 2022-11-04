# Generated by Django 4.1.2 on 2022-11-04 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Order created", "Order Created"),
                            ("Process payment", "Process Payment"),
                            ("Authorized payment", "Authorized Payment"),
                            ("Waiting Shipping", "Waiting Shipping"),
                            ("Sent", "Sent"),
                            ("Order completed", "Order Completed"),
                        ],
                        default="Order created",
                        max_length=40,
                    ),
                ),
                ("shipping", models.IntegerField()),
                ("ammount_items", models.IntegerField()),
                ("total_value", models.IntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
