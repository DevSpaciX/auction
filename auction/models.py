from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class User(AbstractUser):
    money = models.DecimalField(decimal_places=2, max_digits=7, null=True)
    won_item_title = models.CharField(max_length=30,null=True)
    owner_to_chat_with = models.CharField(max_length=30,null=True)


class Auction(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_owner"
    )
    actual_price = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    offered_the_most = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_offered_the_most",
        null=True,
        blank=True
    )
    winner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_winner",blank=True,null=True
    )
    image = models.ImageField(upload_to="images/", default="default.webp")

    def __str__(self):
        return self.title
