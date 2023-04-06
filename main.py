# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time
#
#
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_options)
#
# driver.get('http://orteil.dashnet.org/experiments/cookie/')
#
# items = driver.find_elements(By.CSS_SELECTOR, "#store div")
# item_ids = [item.get_attribute("id") for item in items]
#
# ciastko = driver.find_element(By.ID, "cookie")
#
# timeout = time.time() + 5
# fiveteen_min = time.time() + 60 * 15
#
# while True:
#     ciastko.click()
#     if time.time() > timeout:
#
#         all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
#         item_prices = []
#
#         for price in all_prices:
#             element_text = price.text
#             if element_text != "":
#                 cost = int(element_text.split("-")[1].strip().replace(",", ""))
#                 item_prices.append(cost)
#
#         cookie_upgrades = {}
#         for n in range(len(item_prices)):
#             cookie_upgrades[item_prices[n]] = item_ids[n]
#
#         # Get current cookie count
#         money_element = driver.find_element(By.ID, "money").text
#         if "," in money_element:
#             money_element = money_element.replace(",", "")
#         cookie_count = int(money_element)
#
#         # Find upgrades that we can currently afford
#         affordable_upgrades = {}
#         for cost, id in cookie_upgrades.items():
#             if cookie_count > cost:
#                 affordable_upgrades[cost] = id
#
#         # Purchase the most expensive affordable upgrade
#         highest_price_affordable_upgrade = max(affordable_upgrades)
#         print(highest_price_affordable_upgrade)
#         to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
#
#         driver.find_element(By.ID, to_purchase_id).click()
#
#         # Add another 5 seconds until the next check
#         timeout = time.time() + 5
#
#         # After 5 minutes stop the bot and check the cookies per second count.
#         if time.time() > fiveteen_min:
#             cookie_per_s = driver.find_element(By.ID, "cps").text
#             print(cookie_per_s)
#             break
#
# # price = driver.find_element(By.CLASS_NAME, "a-offscreen+span")
# # print(price.text)
#
#
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('http://orteil.dashnet.org/experiments/cookie/')

item_elements = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [elem.get_attribute("id") for elem in item_elements]

cookie = driver.find_element(By.ID, "cookie")

timeout = time.time() + 5
fifteen_min = time.time() + 60 * 15

while True:
    cookie.click()
    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = [int(price.text.split("-")[1].strip().replace(",", "")) for price in all_prices if price.text != ""]
        cookie_upgrades = {item_prices[n]: item_ids[n] for n in range(len(item_prices))}
        money_element = driver.find_element(By.ID, "money").text.replace(",", "")
        cookie_count = int(money_element)
        affordable_upgrades = {cost: id for cost, id in cookie_upgrades.items() if cookie_count > cost}
        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        driver.find_element(By.ID, to_purchase_id).click()
        timeout = time.time() + 10
        if time.time() > fifteen_min:
            cookie_per_s = driver.find_element(By.ID, "cps").text
            print(cookie_per_s)
            break
