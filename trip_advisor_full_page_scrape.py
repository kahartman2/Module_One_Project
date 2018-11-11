import json
from bs4 import BeautifulSoup
import requests

class ListingBuilder:
    def run(self):
        ta = Scraper()
        names = []
        listings = []
        ta.webpage_html()
        for restaurant in ta.bottom_half():
            x  = Parser(restaurant)
            name = x.restaurant_name()
            num_of_reviews = x.num_of_reviews()
            rating = x.rating()
            address = x.address()
            ranking = x.ranking()
            price = x.price()
            rating_types = x.rating_types()
            listings.append({'Name': name, 'Number of Reviews': num_of_reviews, 'Rating': rating, 'Address': address, 'Ranking':ranking, 'Price': price, 'Rating Types': rating_types})
        print(listings)

class Scraper:
    def webpage_html(self, url = 'https://www.tripadvisor.com/Restaurant_Review-g60763-d1731141-Reviews-Piccola_Cucina-New_York_City_New_York.html'):
        nyc_request = requests.get(url)
        self.timeout_html = nyc_request.text
        return self.timeout_html

    def bottom_half(self, timeout_html = None):
        timeout_html = timeout_html or self.timeout_html
        timeout_soup = BeautifulSoup(timeout_html)
        lower_half =  timeout_soup.findAll('div', {'class': ' non_hotels_like desktop scopedSearch'})
        self.lower_half = lower_half
        return self.lower_half


class Parser:
    def __init__(self, bottom_half):
        self.bottom_half = bottom_half

    def restaurant_name(self):
        return self.bottom_half.find('h1', {'class':'heading_title'}).text

    def address(self):
        street = self.bottom_half.find('span', {'class': 'street-address'}).text
        city_st_zip = self.bottom_half.find('span', {'class': 'locality'}).text
        return street + " " + city_st_zip

    def num_of_reviews(self):
        return self.bottom_half.find('a', {'class':"seeAllReviews"}).text.replace(' reviews', '')

    def rating(self):
        return self.bottom_half.find('span', {'class':'overallRating'}).text

    def cuisines(self):
        return self.bottom_half.find('div', {'class':'text'}).text

    def ranking(self):
        return self.bottom_half.b.text.replace('#', '')

    def price(self):
        return self.bottom_half.find('span', {'class':'header_tags rating_and_popularity'}).text

    def rating_types(self):
        five = self.bottom_half.find_all('span', {'class': 'row_count row_cell'})[0].text
        four = self.bottom_half.find_all('span', {'class': 'row_count row_cell'})[1].text
        three = self.bottom_half.find_all('span', {'class': 'row_count row_cell'})[2].text
        two = self.bottom_half.find_all('span', {'class': 'row_count row_cell'})[3].text
        one = self.bottom_half.find_all('span', {'class': 'row_count row_cell'})[4].text
        return {'5':five, '4':four, '3':three, '2':two, '1':one}
