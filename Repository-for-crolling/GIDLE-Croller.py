from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = "https://www.youtube.com"
driver.get(url)
keyword = "(G)I-DLE (여자)아이들"
driver.find_element(By.CSS_SELECTOR, "#search").click()
driver.find_element(By.CSS_SELECTOR, "#search").send_keys(keyword)
driver.find_element(By.CSS_SELECTOR, "#search").send_keys(Keys.RETURN)

