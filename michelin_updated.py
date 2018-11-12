import requests
from bs4 import BeautifulSoup
import re

class ListingBuilder:
    def run(self):
        to = Scraper()
        to.webpage_html()
        for info in to.main_info():
            to_parser  = Parser(info)
            names = to_parser.restaurant_name()
        return list(map(lambda x: x.text.strip(),names))

class Scraper:

    #gets info from the given url into a text form that can be used
    def webpage_html(self, url = 'https://www.foodandwine.com/news/new-york-city-michelin-stars-2019'):
        timeout_request = requests.get(url)
        self.timeout_html = timeout_request.text
        return self.timeout_html

    def main_info(self, timeout_html = None):

        timeout_html = timeout_html or self.timeout_html
        timeout_soup = BeautifulSoup(timeout_html)
        results =  timeout_soup.findAll('div', {'class': 'padded'})
        self.results = results
        return self.results

class Parser:
    def __init__(self, info):
        self.info = info

    def restaurant_name(self):
        return self.info.findAll('p')[3:78]
