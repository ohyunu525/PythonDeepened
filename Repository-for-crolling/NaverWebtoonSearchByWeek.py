import time
from bs4 import BeautifulSoup
from selenium import webdriver

days = {'월': 'mon', '화': 'tue', '수': 'wed', '목': 'thu', '금': 'fri', '토': 'sat', '일': 'sun'}

def selectDay():
    print("요일을 입력하시오 : ", end="")
    day = input()
    day = days[day]
    return day

days_list = list(days.values())
def calculate_Day():
    t = time.localtime()
    today = time.localtime().tm_wday
    hour = t.tm_hour
    if(t.tm_min >= 40):
        hour += 1

    if(hour >= 23):
        today += 1
    day = days_list[today]
    return day

day = calculate_Day()


url = "https://comic.naver.com/webtoon?tab=" + day
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

lists = soup.find_all('li')
updates = lists.select("ul > li > div > a")

for update in updates :
    find_em_tag = update.find("em")
    if(find_em_tag.attrs['class'] == ['ico_updt']):
        print(update['title'])