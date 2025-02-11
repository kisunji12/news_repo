# news/views.py

import requests
from django.shortcuts import render
from django.conf import settings

def index(request):
   
# Get city data from search box. 

    city = request.GET.get('city')

    if city:
        # Search news by city name using the Currents API search endpoint.
        url = 'https://api.currentsapi.services/v1/search'
        params = {
            'apiKey': settings.CURRENTS_API_KEY,
            'keywords': city,
            'language': 'en'
        }
        response = requests.get(url, params=params)
        data = response.json()
        articles = data.get('news', [])
    else:
        # Display the latest news.
        url = 'https://api.currentsapi.services/v1/latest-news'
        params = {
            'apiKey': settings.CURRENTS_API_KEY,
            'language': 'en'
        }
        response = requests.get(url, params=params)
        data = response.json()
        articles = data.get('news', [])
    context = {'articles': articles}
    return render(request, 'news/index.html', context)

def category_view(request, category):
    """
    View to display news articles for a given category.
    The category (e.g., 'sports', 'entertainment') is passed via the URL.
    """
    url = 'https://api.currentsapi.services/v1/latest-news'
    params = {
        'apiKey': settings.CURRENTS_API_KEY,
        'category': category,
        'language': 'en'
    }
    response = requests.get(url, params=params)
    data = response.json()
    articles = data.get('news', [])
    context = {'articles': articles, 'category': category.title()}
    return render(request, 'news/category.html', context)

def search(request):
    """
    View to handle search queries. The user enters a city name,
    and this view uses the Currents API to retrieve related news.
    """
    city = request.GET.get('city', '')
    articles = []
    if city:
        url = 'https://api.currentsapi.services/v1/search'
        params = {
            'apiKey': settings.CURRENTS_API_KEY,
            'keywords': city,
            'language': 'en'
        }
        response = requests.get(url, params=params)
        data = response.json()
        articles = data.get('news', [])
    context = {'articles': articles, 'city': city}
    return render(request, 'news/search.html', context)
