# Generated by Django 5.0.6 on 2024-06-25 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="nft",
            name="image",
            field=models.ImageField(default="", upload_to="nft/images"),
            preserve_default=False,
        ),
    ]