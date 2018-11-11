from bs4 import BeautifulSoup
import requests

class PageCollector:
    def run(self):
        ta = ScrapeFrontPage()
        listings = []
        ta.webpage_html()
        for restaurant in ta.restaurants():
            url_suffix = restaurant.a.get('href')
            url = "https://www.tripadvisor.com/" + url_suffix
            listings.append(url)
        return listings

class ScrapeFrontPage:
    def webpage_html(self, url = 'https://www.tripadvisor.com/Restaurants-g60763-New_York_City_New_York.html'):
        nyc_request = requests.get(url)
        self.timeout_html = nyc_request.text
        return self.timeout_html

    def restaurants(self, timeout_html = None):
        timeout_html = timeout_html or self.timeout_html
        timeout_soup = BeautifulSoup(timeout_html)
        lower_half =  timeout_soup.findAll('div', {'class': 'ui_column is-9 shortSellDetails'})
        self.lower_half = lower_half
        return self.lower_half
