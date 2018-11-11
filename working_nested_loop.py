import requests
from bs4 import BeautifulSoup
import re

def url_list():
    listings = []
    for i in range(0,330,30):
        url = 'https://www.tripadvisor.com/Restaurants-g60763-oa{}-New_York_City_New_York.html'.format(i)
        request = requests.get(url).text
        soup = BeautifulSoup(request)
        x = soup.findAll('a', {'class': 'property_title'})
        for item in x:
            listings.append(item)
    return listings
'''
        for item in x:
            y = item.find('a', {'class':'property_title'}).get('href')
            listings.append(y)
    return listings

# findAll('a', {'class':'property_title'}.get('href'))

def url_list():
    listings = []
    for i in range(0,300,30):
        url = 'https://www.tripadvisor.com/Restaurants-g60763-oa{}-New_York_City_New_York.html'.format(i)
        request = requests.get(url).text
        soup = BeautifulSoup(request)
        soup.findAll('div', {'class': 'ui_column is-9'})
        for restaurant in soup:
            url_suffix = soup.find('a', {'class':'property_title'}.get('href')).text
            site = "https://www.tripadvisor.com/" + url_suffix
            listings.append(site)
    return listings


        listings = []
        for i in range(0,330,30):
            url = 'https://www.tripadvisor.com/Restaurants-g60763-oa{}-New_York_City_New_York.html'.format(i)
            request = requests.get(url).text
            soup = BeautifulSoup(request)
            x = soup.findAll('div', {'class': 'ui_column is-9'})
        return x
    '''
