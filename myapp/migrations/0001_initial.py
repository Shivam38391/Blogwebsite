# Generated by Django 4.1.3 on 2022-11-27 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=250)),
                ("content", models.TextField()),
                ("last_update", models.DateTimeField(auto_now=True)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="image/")),
            ],
        ),
    ]
