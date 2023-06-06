
from bs4 import BeautifulSoup
import requests

#Constants
URL = "https://www.zillow.com/cary-nc/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A35.94994329518871%2C%22east%22%3A-78.5596748154297%2C%22south%22%3A35.627445464009845%2C%22west%22%3A-79.09937818457033%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A51297%2C%22regionType%22%3A6%7D%5D%7D"
HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accpet-Language":"en-GB,en-US;q=0.9,en;q=0.8"
}
user_response = requests.get(url=URL, headers=HEADER)

class Zillow:
    #URL to the website
    def __init__(self):
        self.html_text = user_response.text
        self.soup = BeautifulSoup(self.html_text, "html.parser")

    def link_to_apartment(self):
        #Using BeautifulSoup to scrape the link of Zillow
        links = self.soup.select('div .property-card-link')
        link_apartment_repeated = [f"https://www.zillow.com{link.get('href')}" for link in links] #list contains twice of each items
        link_apartment = link_apartment_repeated[::1]
        return link_apartment

    def price_for_apartment(self):
        #Using BeautifulSoup to scrape the price from the Zillow
        prices = self.soup.select(".jLQjry")
        price_apartment = []
        for price in prices:
            split_price = price.text.split("+")
            price_apartment.append(split_price[0])
        return price_apartment

    def address_for_apartment(self):
        """Provides address for the apartment"""
        addresses = self.soup.select("address")
        address_apartment = [address.text for address in addresses]
        return address_apartment

