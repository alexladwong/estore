# Generated by Django 4.2.6 on 2023-10-16 21:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("estore", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImageSize",
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
                ("image", models.ImageField(upload_to="your_upload_path/")),
            ],
        ),
        migrations.AddField(
            model_name="cart",
            name="image",
            field=models.ImageField(
                default=django.utils.timezone.now, upload_to="cart_images/"
            ),
            preserve_default=False,
        ),
    ]
