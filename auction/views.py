from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from auction.forms import AuctionForm, AuctionFormCreate
from auction.models import Auction, User


class ListAuctions(generic.ListView):
    template_name = "auction/base.html"
    model = Auction

@login_required
def auction_detail_view(request, pk):
    if request.method == "GET":
        auction = Auction.objects.get(id=pk)
        context = {"auction": auction}
        return render(request, "auction/auction_detail.html", context=context)
    if request.method == "POST":
        creation_form = AuctionForm(request.POST or None)
        new_actual_price = request.POST.get("actual_price")
        auction = Auction.objects.get(pk=pk)
        if creation_form.is_valid() and auction.actual_price < int(new_actual_price):
            user = User.objects.get(username=request.user.username)
            if auction.offered_the_most:
                old_offered_the_most = User.objects.get(username=auction.offered_the_most.username)
                if old_offered_the_most.pk == user.pk:
                    user.money += int(auction.actual_price)
                old_offered_the_most.money += int(auction.actual_price)
                old_offered_the_most.save()

            user.money -= int(new_actual_price)
            user.save()
            auction.actual_price = new_actual_price
            auction.offered_the_most = request.user
            auction.save()
            return HttpResponseRedirect(reverse("auction:list-auctions"))

        else:
            print(creation_form.errors)
            auction = Auction.objects.get(id=pk)
            context = {"error": "Write correct value!", "auction": auction}
            return render(request, "auction/auction_detail.html", context=context)


def auction_delete_view(request, pk):
    auction = Auction.objects.get(id=pk)
    if request.method == "GET":
        context = {"auction": auction}
        return render(request, "auction/confirm_cancel_auction.html", context=context)
    if request.method == "POST":
        if auction.offered_the_most:
            auction.winner = auction.offered_the_most
            user = User.objects.get(pk=auction.winner.id)
            user.won_item_title = auction.title
            user.owner_to_chat_with = auction.owner.username
            user.save()
            Auction.objects.get(id=pk).delete()
        else:
            Auction.objects.get(id=pk).delete()
        return HttpResponseRedirect(reverse("auction:list-auctions"))

class ProfileView(generic.ListView):
    template_name = "auction/profile.html"
    model = get_user_model()


class CreateAuctionView(generic.CreateView):
    template_name = "auction/auction_create.html"
    form_class = AuctionFormCreate
    success_url = reverse_lazy("auction:list-auctions")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner_id = self.request.user.id
        self.object.save()

        return super(CreateAuctionView, self).form_valid(form)