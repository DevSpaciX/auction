from django import forms
from django.forms import ImageField

from auction.models import Auction


class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ["actual_price"]


class AuctionFormCreate(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ["actual_price","title","description","image"]


