import requests
from bs4 import BeautifulSoup as bs

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%A9%94%ED%83%80%EC%9D%B8%EC%82%AC%EC%9D%B4%ED%8A%B8'

response = requests.get(url)
html_text = response.text
soup = bs(html_text, 'html.parser')

title = soup.select_one('a.link_tit').get_text()
sub_title = soup.select_one('a.total_dsc').get_text()
print(title)
print(sub_title)
