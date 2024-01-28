from django.shortcuts import get_object_or_404, render
from .models import Stock
from .scanner import catch_last_pattern

def getStocks():
    stocks = Stock.objects.all().order_by('ticker')
    return stocks

def home(request):
    return render(request, 'home.html')

def stocks(request):
    stocks = getStocks()
    return render(request, 'stocks.html', {'stocks':stocks})

def scanner(request, ticker):
    stock = get_object_or_404(Stock, ticker=ticker)
    result, chart = catch_last_pattern(ticker)
    context = {'stock': stock, 'result':result, 'chart': chart.to_html()}
    return render(request, 'scanner.html', context)