from django.shortcuts import render
from StockExchange.models import Wallet, Asset



def assets_list(request):
    wallets = Wallet.objects.values_list()
    wallests_list_id = [element[0] for element in wallets]
    assets = Asset.objects.filter(wallet__in=wallests_list_id).distinct()

    context = {
        'assets' : assets
    }

    return render(request, 'StockExchange/assets.html', context)
