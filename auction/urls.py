from django.urls import path
from auction.views import ListAuctions, auction_detail_view, auction_delete_view, ProfileView, CreateAuctionView

urlpatterns = [
    path("auctions/", ListAuctions.as_view(), name="list-auctions"),
    path("auctions/<int:pk>", auction_detail_view, name="detail-auctions"),
    path("auctions/delete/<int:pk>", auction_delete_view, name="delete-auctions"),
    path("auctions/profile", ProfileView.as_view(), name="profile"),
    path("auctions/create", CreateAuctionView.as_view(), name="create-auctions"),

]

app_name = "auction"
