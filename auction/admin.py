from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from auction.models import User, Auction

admin.site.register(Auction)


@admin.register(User)
class SuperUser(UserAdmin):
    list_display = UserAdmin.list_display + ("money", "won_item_title", "owner_to_chat_with",)
    fieldsets = UserAdmin.fieldsets + (("User_money", {"fields": ("money","won_item_title", "owner_to_chat_with")}),)
