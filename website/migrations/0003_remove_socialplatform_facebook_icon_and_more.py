# Generated by Django 4.2.11 on 2024-04-14 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0002_socialplatform_facebook_icon_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="socialplatform",
            name="facebook_icon",
        ),
        migrations.RemoveField(
            model_name="socialplatform",
            name="instagram_icon",
        ),
        migrations.RemoveField(
            model_name="socialplatform",
            name="twitter_icon",
        ),
        migrations.RemoveField(
            model_name="socialplatform",
            name="youtube_icon",
        ),
        migrations.AddField(
            model_name="socialplatform",
            name="icon",
            field=models.CharField(
                blank=True,
                choices=[
                    ("fab fa-facebook", "Facebook"),
                    ("fab fa-twitter", "Twitter"),
                    ("fab fa-instagram", "Instagram"),
                    ("fab fa-youtube", "YouTube"),
                ],
                max_length=50,
            ),
        ),
    ]
