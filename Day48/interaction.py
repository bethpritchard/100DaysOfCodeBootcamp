from selenium import webdriver

chrome_driver_path = r"C:\Users\Bethany Pritchard\Dev\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element_by_css_selector("#articlecount a").text

print(article_count)


driver.close()