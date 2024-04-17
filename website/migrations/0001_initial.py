# Generated by Django 4.2.11 on 2024-04-14 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("title", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Featured",
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
                ("title", models.CharField(max_length=100)),
                ("text", models.TextField()),
                ("button_text", models.CharField(max_length=50)),
                ("button_url", models.URLField()),
                ("featured_image", models.ImageField(upload_to="featured_images/")),
                ("background_image", models.ImageField(upload_to="background_images/")),
            ],
        ),
        migrations.CreateModel(
            name="Release",
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
                ("title", models.CharField(max_length=100)),
                ("release_date", models.DateField()),
                (
                    "format",
                    models.CharField(
                        choices=[("LP", "LP"), ("EP", "EP"), ("Single", "Single")],
                        max_length=10,
                    ),
                ),
                (
                    "artwork",
                    models.ImageField(blank=True, upload_to="release_artwork/"),
                ),
                ("spotify_url", models.URLField(blank=True)),
                ("bandcamp_url", models.URLField(blank=True)),
                ("buy_url", models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="SocialPlatform",
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
                ("facebook_url", models.URLField(blank=True)),
                ("twitter_url", models.URLField(blank=True)),
                ("instagram_url", models.URLField(blank=True)),
                ("youtube_url", models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="YouTubeVideo",
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
                ("title", models.CharField(max_length=100)),
                ("url", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Name",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(blank=True, max_length=254)),
                (
                    "contact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="names",
                        to="website.contact",
                    ),
                ),
            ],
        ),
    ]
