# Generated by Django 4.2.2 on 2023-06-21 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(blank=True, max_length=150)),
                ("price", models.IntegerField()),
                ("stock", models.IntegerField()),
            ],
        ),
    ]
