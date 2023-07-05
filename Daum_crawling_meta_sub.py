import requests
from bs4 import BeautifulSoup as bs

# 초기 URL
url = 'https://search.daum.net/search?w=fusion&nil_search=btn&DA=NTB&p=2&q=%EC%A3%BC%EC%8B%9D%ED%99%94%EC%83%81'

# 초기 URL에 접속하여 HTML 문서 가져오기
response = requests.get(url)
html_text = response.text
soup = bs(html_text, 'html.parser')

# <div id="twcColl">에 대한 정보 출력
div_twcColl = soup.find('div', id='twcColl')
print(div_twcColl)

