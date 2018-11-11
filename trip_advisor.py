import json
from bs4 import BeautifulSoup
import requests

class ListingBuilder:
    def run(self):
        ta = Scraper()
        listings = []
        ta.webpage_html()
        for restaurant in ta.restaurants():
            x  = ListingParser(restaurant)
            num_of_reviews = x.num_of_reviews()
            rating = x.rating()
            address = x.address()
            listings.append({'Number of Reviews': num_of_reviews, 'Rating': rating, 'Address': address})
        print(listings)

class Scraper:
    def webpage_html(self, url = 'https://www.tripadvisor.com/Restaurant_Review-g60763-d1731141-Reviews-Piccola_Cucina-New_York_City_New_York.html'):
        nyc_request = requests.get(url)
        self.timeout_html = nyc_request.text
        return self.timeout_html

    def restaurants(self, timeout_html = None):
        timeout_html = timeout_html or self.timeout_html
        timeout_soup = BeautifulSoup(timeout_html)
        lower_half =  timeout_soup.findAll('div', {'class': 'block_wrap easyClear'})
        self.lower_half = lower_half
        return self.lower_half

class ListingParser:
    def __init__(self, listing_html):
        self.listing_html = listing_html

    def address(self):
        street = self.listing_html.find('span', {'class': 'street-address'}).text
        city_st_zip = self.listing_html.find('span', {'class': 'locality'}).text
        return street + " " + city_st_zip

    def num_of_reviews(self):
        return self.listing_html.a.text

    def rating(self):
        return self.listing_html.span.text
