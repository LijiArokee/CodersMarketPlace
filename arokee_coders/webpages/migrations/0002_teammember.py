# Generated by Django 4.1.7 on 2023-03-10 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webpages", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TeamMember",
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
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("role", models.CharField(max_length=255)),
                ("linkedin_link", models.CharField(max_length=255)),
                ("email", models.CharField(max_length=255)),
                ("photo", models.ImageField(upload_to="media/team/%Y/%m")),
                ("created_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
