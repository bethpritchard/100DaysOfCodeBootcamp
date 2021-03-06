from data_entry import FormManager
from data_scraping import DataScraper

data_scraper = DataScraper()
addresses = data_scraper.addresses
links = data_scraper.links
prices = data_scraper.prices

form_manager = FormManager()

for i in range(len(addresses)):
    form_manager.enter_data(address=addresses[i], price=prices[i], link=links[i])


print("Data submitted.")