from django.shortcuts import render
import requests
from decouple import config
# json daha iyi formatta yazdirmak icin
from pprint import pprint
from .models import City

def index(request):
    cities=City.objects.all()
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'
    # pprint(content)
    # print(type(content))
    
    for city in cities:
        print(city)
        response = requests.get(url.format(city, config('API_KEY')))
        content= response.json()
        pprint(content)
        
    return render(request, 'weatherapp/index.html')

