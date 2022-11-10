# Generated by Django 4.1.2 on 2022-11-07 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0001_initial"),
        ("books", "0004_alter_book_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="books",
                to="categories.categories",
            ),
        ),
    ]
