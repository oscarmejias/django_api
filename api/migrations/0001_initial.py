# Generated by Django 5.0.1 on 2024-01-16 17:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patient",
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
                ("name", models.CharField(max_length=50)),
                ("patient_ID", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=20)),
            ],
        ),
    ]
