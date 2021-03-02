from selenium import webdriver

chrome_driver_path = r"C:\Users\Bethany Pritchard\Dev\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get("https://www.python.org/")
# # price = driver.find_element_by_id("priceblock_ourprice")
# # print(price.text)
#
#
# bug_link = driver.find_element_by_xpath('/html/body/div/footer/div[2]/div/ul/li[3]/a')
#
# print(bug_link.text)
#
#

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")

events = {i: {"time": event_times[i].text, "name": event_names[i].text} for i in range(len(event_times))}
print(events)



driver.close()
