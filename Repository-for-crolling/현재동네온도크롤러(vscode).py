from urllib import request, parse
from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.naver.com/').text
soup = BeautifulSoup(html, 'html.parser')

title_list = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')

for i, title in enumerate(title_list):
    print(i+1, title.text)
