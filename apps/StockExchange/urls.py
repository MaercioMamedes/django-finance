from django.urls import path
from StockExchange.views import create_wallet

urlpatterns = [
    path('create-wallet',create_wallet, name='create_wallet'),
]