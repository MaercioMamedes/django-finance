from StockExchange.helpers import factor_asset
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages
from StockExchange.models import Wallet, Asset
from appUsers.models import User

def create_wallet(request):
    if  request.user.is_anonymous:
        return redirect('core:login')

    else:

        user = User.objects.get(id=request.user.id)
        wallet = Wallet.objects.get(user=user.id)

        if request.method == 'POST':
            code_ticker = request.POST['ticker'].upper() + '.SA'
            try:
                asset=get_object_or_404(Asset, ticker=code_ticker)
                wallet.assets_wallet.add(asset)
                messages.success(request,"Papel adicionado")


            except:
                
                try:
                    asset = factor_asset(code_ticker)
                    if asset is None:
                        raise Http404

                except:
                    messages.error(request, 'Papel não encontrado na base de dados')
                
            #Asset.create_asset(code_ticker)

        context = {
            'user' : user,
            'wallet' : wallet.assets_wallet.values(),
        }

    
        return render(request,'StockExchange/createWallet.html', context)