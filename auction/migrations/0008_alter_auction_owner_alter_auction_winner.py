# Generated by Django 4.1.5 on 2023-01-12 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auction", "0007_alter_auction_actual_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="auction",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_owner",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="auction",
            name="winner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_winner",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
