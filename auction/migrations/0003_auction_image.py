# Generated by Django 4.1.3 on 2023-01-11 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auction", "0002_alter_user_money"),
    ]

    operations = [
        migrations.AddField(
            model_name="auction",
            name="image",
            field=models.ImageField(default="default.webp", upload_to="images/"),
        ),
    ]
