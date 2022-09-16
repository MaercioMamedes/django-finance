from django.shortcuts import render, redirect
from StockExchange.models import Asset

def create_wallet(request):
    if  request.user.is_anonymous:
        return redirect('core:login')
    ticker = Asset.objects.all()[0]

    if request.method == 'POST':
        code_ticker = request.POST['ticker']+'.SA'
        Asset.create_asset(code_ticker)

    tickers = Asset.objects.all()
    papel = {'tickers':tickers}
    

    return render(request,'StockExchange/createWallet.html', papel)