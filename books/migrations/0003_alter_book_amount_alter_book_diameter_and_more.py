# Generated by Django 4.1.2 on 2022-11-07 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="amount",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="book",
            name="diameter",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="book",
            name="format",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="book",
            name="length",
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name="book",
            name="weigth",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="book",
            name="width",
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
