from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from myapp import support_functions
from myapp.models import Currency, AccountHolder, Whisky, WhiskyBooze, Whisky2, WhiskyBooze2

from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def home(request):
    data = dict()
    import datetime
    time = datetime.datetime.now()
    data["time_of_day"] = time
    print(time)
    return render(request, "home.html", context=data)

def maintenance(request):
    data = dict()
    return render(request,"maintenance.html",context=data)

def maintenance(request):
    data = dict()
    try:
        choice = request.GET['selection']
        if choice == "currencies":
            support_functions.add_currencies(support_functions.get_currency_list())
            c_list = Currency.objects.all()
            print("Got c_list",len(c_list))
            data['currencies'] = c_list
            return HttpResponseRedirect(reverse('currencies'))
    except:
        pass
    return render(request,"maintenance.html",context=data)

def view_currencies(request):
    data = dict()
    c_list = Currency.objects.all()
    data['currencies'] = c_list
    return render(request,'currencies.html',context=data)

def whiskymaintenance(request):
    data = dict()
    try:
        choice = request.GET['selection']
        if choice == "whiskies":
            support_functions.add_whiskies(support_functions.get_whisky_list())
            w_list = Whisky.objects.all()
            print("Got w_list", len(w_list))
            data['whiskies'] = w_list
            return HttpResponseRedirect(reverse('whiskies'))
        elif choice == "whiskies_booze":
            support_functions.add_whiskies_booze(support_functions.get_whisky_list_booze())
            wb_list = WhiskyBooze.objects.all()
            print("Got wb_list", len(wb_list))
            data['whiskies_booze'] = wb_list
            return HttpResponseRedirect(reverse('whiskies_booze'))
        elif choice == "delete_whiskies":
            support_functions.delete_all()
            return HttpResponseRedirect(reverse('whisky_selector'))
    except:
        pass
    return render(request,"whiskymaintenance.html",context=data)

def view_pricesA(request):
    data = dict()
    w_list = Whisky.objects.all()
    data['whiskies'] = w_list
    return render(request,'pricesA.html',context=data)

def view_pricesB(request):
    data = dict()
    wb_list = WhiskyBooze.objects.all()
    data['whiskies_booze'] = wb_list
    return render(request,'pricesB.html',context=data)

def register_new_user(request):
    context = dict()
    form = UserCreationForm(request.POST)
    if form.is_valid():
        print("valid form")
        new_user = form.save()
        dob = request.POST["dob"]
        acct_holder = AccountHolder(user=new_user,date_of_birth=dob)
        acct_holder.save()
        return render(request,"home.html",context=dict())
    else:
        form = UserCreationForm()
        context['form'] = form
        return render(request, "registration/register.html", context=context)

def currency_selection(request):
    data = dict()
    currencies =Currency.objects.all()
    data['currencies'] = currencies
    return render(request,"currency_selector.html",data)

def exch_rate(request):
    data=dict()
    try:
        currency1 = request.GET['currency_from']
        currency2 = request.GET['currency_to']
        c1 = Currency.objects.get(iso=currency1)
        c2 = Currency.objects.get(iso=currency2)
        data['currency1'] = c1
        data['currency2'] = c2
        try:
            rate = c1.rates_set.get(x_currency=c2.iso).rate
            data['rate'] = rate
        except:
            data['rate'] = "Not Available"
    except:
        pass
    return render(request,"exchange_detail.html",data)

def whisky_selection(request):
    data = dict()
    whiskies =Whisky.objects.all()
    whiskies_booze = WhiskyBooze.objects.all()
    data['whiskies'] = whiskies
    data['whiskies_booze']= whiskies_booze
    return render(request,"whisky_selector.html",data)

def whisky_selection2(request):
    data = dict()
    user = request.user
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    whiskies2 =Whisky2.objects.all()
    whiskies_booze2 = WhiskyBooze2.objects.all()
    data['whiskies2'] = whiskies2
    data['whiskies_booze2']= whiskies_booze2
    data['user'] = user
    return render(request,"whisky_selector2.html",data)

def whisky_price(request):
    data=dict()
    whiskyA = request.GET['whisky_A']
    whiskyB = request.GET['whisky_B']
    w1 = Whisky.objects.get(item_name=whiskyA)
    w2 = WhiskyBooze.objects.get(item_name=whiskyB)
    data['whiskyA'] = w1
    data['whiskyB'] = w2

    return render(request,"price_detail.html",data)

def view_beginners(request):
    return render(request, 'beginners.html', context={})

def view_pricesA2(request):
    data = dict()
    w_list2 = Whisky2.objects.all()
    data['whiskies2'] = w_list2
    return render(request,'priceA2.html',context=data)

def view_pricesB2(request):
    data = dict()
    wb_list2 = WhiskyBooze2.objects.all()
    data['whiskies_booze2'] = wb_list2
    return render(request,'priceB2.html',context=data)

def whiskymaintenance2(request):
    data = dict()
    try:
        choice = request.GET['selection']
        if choice == "whiskies2":
            support_functions.add_whiskies2(support_functions.get_whisky_list2())
            w_list = Whisky2.objects.all()
            print("Got w_list", len(w_list))
            data['whiskies2'] = w_list
            return HttpResponseRedirect(reverse('whiskies2'))
        elif choice == "whiskies_booze2":
            support_functions.add_whiskies_booze2(support_functions.get_whisky_list_booze2())
            wb_list = WhiskyBooze2.objects.all()
            print("Got wb_list", len(wb_list))
            data['whiskies_booze2'] = wb_list
            return HttpResponseRedirect(reverse('whiskies_booze2'))
        elif choice == "delete_whiskies":
            support_functions.delete_all()
            return HttpResponseRedirect(reverse('whisky_selector2'))
    except:
        pass
    return render(request,"whiskymaintenance2.html",context=data)

def whisky_price2(request):
    data=dict()
    whiskyA = request.GET['whisky_A']
    whiskyB = request.GET['whisky_B']
    w1 = Whisky2.objects.get(item_name=whiskyA)
    w2 = WhiskyBooze2.objects.get(item_name=whiskyB)
    data['whiskyA'] = w1
    data['whiskyB'] = w2

    return render(request,"price_detail2.html",data)
