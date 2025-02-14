# Generated by Django 4.2 on 2023-04-13 10:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hirecoder",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("coder_id", models.IntegerField()),
                ("coder_name", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("message", models.TextField(max_length=100)),
                ("user_id", models.IntegerField(blank=True)),
                (
                    "created_date",
                    models.DateTimeField(blank=True, default=datetime.datetime.now),
                ),
            ],
        ),
    ]
