import requests
from bs4 import BeautifulSoup
import re

class ScrapeFrontPage:
    def webpage_html(self, url = 'https://www.yelp.com/search?find_loc=New+York,+NY&start=0&cflt=restaurants'):
        nyc_request = requests.get(url)
        self.timeout_html = nyc_request.text
        return self.timeout_html

    def restaurants(self, timeout_html = None):
        timeout_html = timeout_html or self.timeout_html
        timeout_soup = BeautifulSoup(timeout_html)
        lower_half =  timeout_soup.findAll('span', {'class': 'indexed-biz-name'})
        self.lower_half = lower_half
        return self.lower_half

class PageCollector:
    #scans the rankings page to pull the individual restaurant's url
    def run(self):
        ta = ScrapeFrontPage()
        page_listings = []
        ta.webpage_html()
        all_restaurants = ta.restaurants()
        for restaurant in all_restaurants:
            url_suffix = str(restaurant.a.get('href'))
            url = 'https://yelp.com' + url_suffix
            page_listings.append(url)
        return page_listings
