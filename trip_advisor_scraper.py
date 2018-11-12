import requests
from bs4 import BeautifulSoup

class ListingBuilder:
    def run_scraper(self):
        ta = Scraper()
        for restaurant in ta.url_list():
            listings = []
            ta.webpage_html(restaurant)
            for restaurant in ta.listing_page():
                x  = Parser(restaurant)
                name, num_of_reviews, rating, address  = x.restaurant_name(), x.num_of_reviews(), x.rating(), x.address(),
                cuisines, ranking, price, rating_types_percent = x.cuisines(), x.ranking(), x.price(), x.rating_types_percent()
                keys = ['Name', 'Ranking', 'Rating', 'Number of Reviews', 'Address', 'Cuisines',  'Price', 'Rating Types']
                values = [name, ranking, rating, num_of_reviews, address, cuisines, price, rating_types_percent]
                listings.append(dict(zip(keys, values)))
            print(listings)

class Scraper:
    def webpage_html(self, url):
        nyc_request = requests.get(url)
        self.trip_advisor_html = nyc_request.text
        return self.trip_advisor_html

    def listing_page(self, trip_advisor_html = None):
        trip_advisor_html = trip_advisor_html or self.trip_advisor_html
        timeout_soup = BeautifulSoup(trip_advisor_html)
        individual_listing =  timeout_soup.findAll('div', {'class': ' non_hotels_like desktop scopedSearch'})
        self.individual_listing = individual_listing
        return self.individual_listing

    def url_list(self):
        self.individual_listing_urls = []
        for i in range(0,400,30):
            url = 'https://www.tripadvisor.com/Restaurants-g60763-oa{}-New_York_City_New_York.html'.format(i)
            request = requests.get(url).text
            soup = BeautifulSoup(request)
            x = soup.findAll('a', {'class': 'property_title'})
            for item in x:
                prefix = 'https://www.tripadvisor.com/'
                suffix = item.get('href')
                self.individual_listing_urls.append(prefix + suffix)
        return self.individual_listing_urls

class Parser:
    def __init__(self, listing_page):
        self.listing_page = listing_page

    def restaurant_name(self):
        return self.listing_page.find('h1', {'class':'heading_title'}).text

    def address(self):
        street = self.listing_page.find('span', {'class': 'street-address'}).text
        city_st_zip = self.listing_page.find('span', {'class': 'locality'}).text
        return street + " " + city_st_zip

    def num_of_reviews(self):
        return int(self.listing_page.find('a', {'class':"seeAllReviews"}).text.replace(' reviews', ''))

    def rating(self):
        return float(self.listing_page.find('span', {'class':'overallRating'}).text)

    def cuisines(self):
        return self.listing_page.find('span', {'class':'header_links rating_and_popularity'}).text.split(',')

    def ranking(self):
        return int(self.listing_page.b.text.replace('#', ''))

    def price(self):
        return self.listing_page.find('span', {'class':'header_tags rating_and_popularity'}).text

    def rating_types_percent(self):
        five = self.listing_page.find_all('span', {'class': 'row_count row_cell'})[0].text.replace('%','')
        four = self.listing_page.find_all('span', {'class': 'row_count row_cell'})[1].text.replace('%','')
        three = self.listing_page.find_all('span', {'class': 'row_count row_cell'})[2].text.replace('%','')
        two = self.listing_page.find_all('span', {'class': 'row_count row_cell'})[3].text.replace('%','')
        one = self.listing_page.find_all('span', {'class': 'row_count row_cell'})[4].text.replace('%','')
        return {'5-Star':int(five), '4-Star':int(four), '3-Star':int(three), '2-Star':int(two), '1-Star':int(one)}
