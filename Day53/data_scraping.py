
from bs4 import BeautifulSoup
import  requests


zillow_url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

class DataScraper:

    def __init__(self):
        headers = {
    "Accept-Language": "en-GB,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
}
        self.response = requests.get(url=zillow_url, headers=headers)
        zillow_site = self.response.text
        self.soup = BeautifulSoup(zillow_site, "html.parser")

        # Collect links
        self.link_soup = self.soup.select(".list-card-top a")
        self.links_init = [link["href"] for link in self.link_soup]

        self.links = []

        for link in self.links_init:
            if "zillow" not in link:
                self.links.append("https://www.zillow.com" + link)
            else:
                self.links.append(link)

        # Collect prices
        price_soup = self.soup.select(".list-card-heading")
        self.prices_text = []

        for element in price_soup:
            # Get the prices. Single and multiple listings have different tag & class structures
            try:
                # Price with only one listing
                price = element.select(".list-card-price")[0].contents[0]
            except IndexError:
                print('Multiple listings for the card')
                # Price with multiple listings
                price = element.select(".list-card-details li")[0].contents[0]
            finally:
                self.prices_text.append(price)

        self.prices = [self.split_price(price) for price in self.prices_text]

        # Collect addresses

        self.address_soup = self.soup.find_all(name= "address", class_ ="list-card-addr")
        self.addresses = [address.text.split(" | ")[-1] for address in self.address_soup]

    @staticmethod
    def split_price(price):
        if "+" in price:
            split_elem = "+"
        elif "/" in price:
            split_elem = "/"
        else:
            split_elem = " "

        return price.split(split_elem)[0]
