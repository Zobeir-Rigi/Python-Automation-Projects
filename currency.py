import requests
API_KEY = 'fca_live_WaNVuedUnJPSFHwMvmzoytJdrXiHhDYebZJQEo9N'  #capital, because it's a const.
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}' #Because of Authorization. It's $ instead of f in JS.


CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]

# defining a function to format the url
def convert_currency(base): 
    currencies = ",".join(CURRENCIES) #In JS => const currencies = CURRENCIES.join(',');
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
   #try catch in JS, accessing data by fetching
    try: 
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Invalid currency.")
        return None

 base = input("Enter the base currency (q for quit): ").upper()


data = convert_currency(base)
del data[base]
# Python dictionaries(ticker & value) = objects in JS (key & value)
for ticker, value in data.items():
    print(F"{ticker}:{value}")


