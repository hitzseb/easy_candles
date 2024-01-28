from django.urls import path
from .views import home, stocks, scanner

urlpatterns = [
    path('', home, name='home'),
    path('stocks', stocks, name='stocks'),
    path('scanner/<str:ticker>/', scanner, name='scanner'),
]