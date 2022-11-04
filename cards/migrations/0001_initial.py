# Generated by Django 4.1.2 on 2022-11-04 17:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Card",
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
                ("card_name", models.CharField(max_length=25)),
                ("number_card", models.CharField(max_length=16)),
                ("expire_date", models.CharField(max_length=6)),
            ],
        ),
    ]
