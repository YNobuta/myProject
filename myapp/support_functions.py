from myapp.models import Currency, Whisky


def get_currency_list():
    currency_list = list()
    import requests
    from bs4 import BeautifulSoup
    url = "https://thefactfile.org/countries-currencies-symbols/"
    response = requests.get(url)
    if not response.status_code == 200:
        return currency_list
    soup = BeautifulSoup(response.content)
    data_lines = soup.find_all('tr')
    for line in data_lines:
        try:
            detail = line.find_all('td')
            currency = detail[2].get_text().strip()
            iso = detail[3].get_text().strip()
            if (currency,iso) in currency_list:
                continue
            currency_list.append((currency,iso))
        except:
            continue
    return currency_list

def add_currencies(currency_list):
    for currency in currency_list:
        currency_name = currency[0]
        currency_symbol = currency[1]
        if len(currency_symbol) > 3:
            continue
        try:
            c= Currency.objects.get(iso=currency_symbol)
        except:
            c = Currency(long_name=currency_name, iso=currency_symbol)
            c.save()  #To test out the code, replace this by print(c)


def get_whisky_list():
    import requests
    from bs4 import BeautifulSoup
    url = "https://www.nationwideliquor.com/products/japanese-whisky"
    response = requests.get(url)
    soup = BeautifulSoup(response.content)
    data_names = soup.find_all('a', {"class": "product_title"})
    data_prices = soup.find_all('div', {"class": "pb_price"})

    list_names = []
    for name in data_names:
        list_names.append(name.get_text().strip())

    list_prices = []
    for price in data_prices:
        list_prices.append(price.get_text().strip())

    list_marged = list(zip(list_names, list_prices))
    return list_marged

def add_whiskies(whisky_list):
    for whisky in whisky_list:
        whisky_name = whisky[0]
        whisky_price = whisky[1]
        try:
            w= Whisky.objects.get(item_name=whisky_name)
        except:
            w = Whisky(item_name=whisky_name, price=whisky_price)
            w.save()  #To test out the code, replace this by print(c)
            # print(w)
