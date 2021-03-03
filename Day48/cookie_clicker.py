from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = r"C:\Users\Bethany Pritchard\Dev\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

all_items = driver.find_elements_by_css_selector("#store div")
unavail_items = driver.find_elements_by_class_name("grayed")

timer = 0
timeout = time.time() + 5
end_time = time.time() + (5 * 60)
click_cookie = True
item_clicked = False

mine = driver.find_element_by_css_selector("#buyMine")
mine_lst = mine.text.split(" ")[2].split("\n")[0].strip().split(",")
mine_cost = int(mine_lst[0] + mine_lst[1])

while click_cookie:
    cookie.click()
    if time.time() > timeout:
        avail_items = []
        all_items = driver.find_elements_by_css_selector("#store div")
        unavail_items = driver.find_elements_by_class_name("grayed")
        for item in all_items:
            if item not in unavail_items:
                avail_items.append(item)

        cps_text = driver.find_element_by_css_selector("#cps")
        cps = cps_text.text.split(":")[-1].strip()
        #
        for i in range(len(avail_items) - 1, 1, -1):
            try:
                avail_items[i].get_attribute("onclick")
                avail_items[i].click()
            except:
                pass
        # if len(avail_items) > 2:
        #     avail_items[-1].get_attribute("onclick")
        #     avail_items[-1].click()
        # if float(cps) < 20:
        #     timeout += 5
        # elif float(cps) < 30:
        #     timeout += 10
        # elif float(cps) < 50:
        #     timeout += 15
        # elif float(cps) < 70:
        #     timeout += 20

        timer = +1
        if timer < 6:

        elif 6<timer<20:
            timeout += 15
        elif 20<timer<30:
            timeout += 25

    if time.time() > end_time:
        avail_items = driver.find_elements_by_css_selector("#store div")
        for i in range(len(avail_items) - 1, 0, -1):
            try:
                avail_items[i].get_attribute("onclick")
                avail_items[i].click()
            except:
                pass
        click_cookie = False

cps = driver.find_element_by_css_selector("#cps")

with open("score.txt", "a+") as fp:
    fp.write(cps.text + "\n")

print(cps.text)
