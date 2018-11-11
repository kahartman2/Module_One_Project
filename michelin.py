import requests
from bs4 import BeautifulSoup
import re

#gathers list of names of all Michelin rated restaurants in NYC
class ListingBuilder:
    def run(self):
        to = Scraper()
        listings = []
        to.webpage_html()
        for info in to.main_info():
            to_parser  = Parser(info)
            name = to_parser.restaurant_name()
            listings.append(name)
        print(listings)

class Scraper:

    #gets info from the given url into a text form that can be used
    def webpage_html(self, url = 'https://www.timeout.com/newyork/restaurants/michelin-starred-restaurants-in-nyc'):
        timeout_request = requests.get(url)
        self.timeout_html = timeout_request.text
        return self.timeout_html

    def main_info(self, timeout_html = None):

        timeout_html = timeout_html or self.timeout_html
        timeout_soup = BeautifulSoup(timeout_html)
        results =  timeout_soup.findAll('h3', {'class': 'card-title'})
        self.results = results
        return self.results

class Parser:
    def __init__(self, info):
        self.info = info

    def restaurant_name(self):
        return self.info.a.text.strip()
