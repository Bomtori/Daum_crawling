import requests
from bs4 import BeautifulSoup as bs

# 초기 URL
url = 'https://search.daum.net/search?w=fusion&nil_search=btn&DA=NTB&p=2&q=%EB%A9%94%ED%83%80%EC%9D%B8%EC%82%AC%EC%9D%B4%ED%8A%B8'

# 초기 URL에 접속하여 HTML 문서 가져오기
response = requests.get(url)
html_text = response.text
soup = bs(html_text, 'html.parser')

# <div id="twcColl">에 대한 정보 출력
div_twcColl = soup.find('div', id='twcColl')
print(div_twcColl)

