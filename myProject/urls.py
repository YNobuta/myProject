"""myProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("",views.home, name="home"),
    path('home',views.home, name='home1'),
    path('maintenance',views.maintenance,name='maintenance'),
    path('currencies',views.view_currencies, name='currencies'),
    path('currency-selection',views.currency_selection,name="currency_selector"),
    path('exchange_rate_info',views.exch_rate,name="exchange_rate_info"),
    path('whiskymaintenance',views.whiskymaintenance,name='whiskymaintenance'),
    path('whiskymaintenance2',views.whiskymaintenance2,name='whiskymaintenance2'),
    path('register',views.register_new_user,name="register_user"),
    path('whisky-selection',views.whisky_selection,name="whisky_selector"),
    path('whisky-selection2',views.whisky_selection2,name="whisky_selector2"),
    path('whisky_price_info',views.whisky_price,name="whisky_price_info"),
    path('whisky_price_info2',views.whisky_price2,name="whisky_price_info2"),
    path('pricesA',views.view_pricesA, name='whiskies'),
    path('pricesB',views.view_pricesB, name='whiskies_booze'),
    path('priceA2', views.view_pricesA2, name='whiskies2'),
    path('priceB2', views.view_pricesB2, name='whiskies_booze2'),
    path('beginners',views.view_beginners, name='beginners'),
]

