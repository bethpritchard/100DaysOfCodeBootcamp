from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"C:\Users\Bethany Pritchard\Dev\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
last_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
sign_up = driver.find_element_by_css_selector(".btn")

first_name.send_keys("Beth")
last_name.send_keys("Pritchard")
email.send_keys("myemail123@gmail.com")
sign_up.click()