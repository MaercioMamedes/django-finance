from django.urls import path
from apps.StockExchange.views import create_wallet
from apps.StockExchange.views.assets_list import assets_list
from apps.StockExchange.views.delete_asset import delete_asset

urlpatterns = [
    path('create-wallet', create_wallet, name='create_wallet'),
    path('delete-asset/<int:id>', delete_asset, name='delete_asset'),
    path('assets', assets_list, name='assets_list'),
]