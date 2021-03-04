from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = r"C:\Users\Bethany Pritchard\Dev\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")
url = "https://www.linkedin.com/jobs/search/?currentJobId=2424262028&f_L=United%20Kingdom&geoId=101165590&keywords=python%20developer&location=United%20Kingdom"

driver.get(url)

time.sleep(2)

sign_in = driver.find_element_by_css_selector("a" ".nav__button-secondary")
sign_in.click()

time.sleep(2)

email_box = driver.find_element_by_id("username")
email_box.send_keys(email)

password_box = driver.find_element_by_id("password")
password_box.send_keys(password)

password_box.send_keys(Keys.ENTER)

time.sleep(15)

first_job = driver.find_element_by_class_name("jobs-save-button artdeco-button artdeco-button--3 artdeco-button--secondary")
first_job.click()
