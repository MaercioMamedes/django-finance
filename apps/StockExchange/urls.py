from django.urls import path
from StockExchange.views import create_wallet
from apps.StockExchange.views.delete_asset import delete_asset

urlpatterns = [
    path('create-wallet',create_wallet, name='create_wallet'),
    path('delete-asset/<int:id>',delete_asset, name='delete_asset'),
    
]