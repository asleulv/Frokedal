# Generated by Django 4.2.11 on 2024-04-16 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0014_alter_featured_background_image_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="featured",
            name="is_dark_text",
            field=models.BooleanField(default=True),
        ),
    ]
