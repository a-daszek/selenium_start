from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.amazon.com/Logitech-LIGHTSPEED-Wireless-Gaming-Mouse/dp/B07CMS5Q6N/ref=sr_1_3?keywords=gaming%2Bmouse&pd_rd_r=63f31e37-7ca5-40bb-9826-b8b7ea282dcc&pd_rd_w=Bopxl&pd_rd_wg=SXcFo&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=C6BR01C90S3BZG5QWFZ0&qid=1680774111&refinements=p_89%3ALogitech%2BG%7CSteelSeries%2Cp_n_feature_two_browse-bin%3A23473577011%2Cp_n_feature_eight_browse-bin%3A23627257011&rnid=23627253011&s=videogames&sr=1-3&th=1')

price = driver.find_element(By.CLASS_NAME, "a-offscreen+span")
print(price.text)


