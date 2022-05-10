from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time

driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
driver.implicitly_wait(2)
driver.get('https://www.dhlottery.co.kr/gameResult.do?method=byWin')
action = ActionChains(driver)
time.sleep(2)


btns = driver.find_element_by_css_selector(".btns_function.bottom.border")

btns.find_element_by_name('drwNoStart').click()
time.sleep(0.5)
action.key_down(Keys.END).key_down(Keys.ENTER).perform()
time.sleep(0.5)


btns.find_element_by_name('drwNoEnd').click()
time.sleep(0.5)
action.key_down(Keys.HOME).key_down(Keys.ENTER).perform()
time.sleep(0.5)


btns.find_element_by_id('exelBtn').click()
time.sleep(0.5)

# df = pd.read_excel("C:/Users/CFLAB/Downloads/excel.xls")
df = pd.read_html("C:/Users/jey25/Downloads/excel.xls")
print(df)