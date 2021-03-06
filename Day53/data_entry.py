import time

from selenium import webdriver

form_url = "https://forms.gle/FrT5bd5YFqk4mi3n7"


class FormManager:
    def __init__(self):
        chrome_driver_path = r"C:\Users\Bethany Pritchard\Dev\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.maximize_window()
        self.driver.get(form_url)

    def enter_data(self, address, price, link):
        time.sleep(1)
        address_box = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_box.send_keys(address)

        price_box = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_box.send_keys(price)

        link_box = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_box.send_keys(link)

        time.sleep(1)

        submit = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
        submit.click()

        time.sleep(1)

        submit_another = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        submit_another.click()
