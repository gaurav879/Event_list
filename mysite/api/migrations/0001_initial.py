# Generated by Django 4.0 on 2021-12-24 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("event_name", models.CharField(max_length=255)),
                ("data", models.CharField(max_length=255)),
                ("time", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("is_liked", models.BooleanField(max_length=255)),
                ("image", models.CharField(max_length=255)),
            ],
        ),
    ]
