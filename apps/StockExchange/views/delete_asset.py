from gc import get_objects
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from apps.StockExchange.models import Wallet, Asset


def delete_asset(request, id):
    asset = get_object_or_404(Asset, id=id)

    try:

        wallet = get_object_or_404(Wallet, user=request.user.id)
        wallet.assets_wallet.remove(asset)
        messages.info(request, f'O papel {asset.ticker} excluído com sucesso')
    except:

        messages.error(request, 'Operação não permitida')

    return redirect('create_wallet')
