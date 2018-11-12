import requests
from bs4 import BeautifulSoup
import re

class ListingBuilder:
    def run(self):
        inf = Scraper()
        listings = []
        for x in range(1,53):
            inf.webpage_html(str(x))
            for info in inf.restaurants_html():
                for i in range(0,16):
                    inf_parser  = Parser(info)
                    name = inf_parser.restaurant_name(i)
                    neighborhood = inf_parser.restaurant_neighborhood(i)
                    rating = inf_parser.restaurant_rating(i)
                    price = inf_parser.restaurant_price(i)
                    listings.append({'Name':name, 'Neighborhood': neighborhood,'Rating': rating, 'Price': price})
        print(listings)

class Scraper:
    def webpage_html(self, url_suffix):
        url_prefix = 'https://www.theinfatuation.com/new-york/reviews?sort=&page='
        url = url_prefix + url_suffix
        timeout_request = requests.get(url)
        self.timeout_html = timeout_request.text
        return self.timeout_html

    def restaurants_html(self, timeout_html = None):
        timeout_html = timeout_html or self.timeout_html
        timeout_soup = BeautifulSoup(timeout_html)
        lower_half =  timeout_soup.findAll('div', {'id': 'list'})
        self.lower_half = lower_half
        return self.lower_half

class Parser:
    def __init__(self, info):
            self.info = info

    def restaurant_name(self, i):
        name = self.info.findAll('a',{'class':'feature__title'})[i].h3.text
        return name

    def restaurant_neighborhood(self, i):
        neighborhood = self.info.findAll('div',{'class':'review-table__neighborhood'})[i].text
        return neighborhood

    def restaurant_rating(self, i):
        rating = self.info.findAll('div',{'class':'review-table__rating'})[i].text.strip()
        return rating

    def restaurant_price(self, i):
        price = self.info.findAll('div',{'class':'price-rating'})[i].text.strip()
        return price
