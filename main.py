import os
# import pandas as pd
# # from fake_useragent import UserAgent

# from selenium import webdriver
# import pandas as pd


# driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"))
# driver.get("https://www.nrl.com/draw/nrl-premiership/2022/round-16/sea-eagles-v-storm/")

# driver.implicitly_wait(30)

# html = driver.page_source

# tables = pd.read_html(html)
# data = tables[0]
# print(data)

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
import pandas as pd

WAIT_TIME = 10
driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"))
# driver.implicitly_wait(30)

driver.get("https://www.nrl.com/draw/nrl-premiership/2022/round-16/sea-eagles-v-storm/")

# time.sleep(10)
element = WebDriverWait(driver, WAIT_TIME).until (
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#tabs-match-centre- > div.l-grid > div > div > ul > li:nth-child(5) > a"))
)
element.click()

df=pd.read_html(driver.find_element_by_id("player-stats").get_attribute('outerHTML'))[0]
print(df)
df.to_csv('table-2.csv')

time.sleep(3)
element = WebDriverWait(driver, WAIT_TIME).until (
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#tabs-match-centre-4 > section > div > div > div.button-group.u-flex-align-self-center.u-spacing-mb-medium > div.button-group-item.u-width-50.t-local-storm > button"))
)
element.click()

df=pd.read_html(driver.find_element_by_id("player-stats").get_attribute('outerHTML'))[0]
print(df)
df.to_csv('table-1.csv')

driver.close()
