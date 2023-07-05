import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# 데이터를 저장할 빈 리스트 생성
제목들 = []
내용들 = []
링크들 = []
날짜들 = []

# 초기 URL
url = 'https://search.daum.net/search?w=fusion&nil_search=btn&DA=NTB&p=1&q=%EB%A9%94%ED%83%80%EC%9D%B8%EC%82%AC%EC%9D%B4%ED%8A%B8'

# 초기 URL에 접속하여 HTML 문서 가져오기
response = requests.get(url)
html_text = response.text
soup = bs(html_text, 'html.parser')

# <div id="twcColl">에 대한 정보 출력
div_twcColl = soup.find('div', id='twcColl')

# <c-menu-share> 요소들을 모두 찾습니다.
c_menu_shares = div_twcColl.find_all('c-menu-share')

date_elements = soup.find_all(name='c-frag', attrs={'slot': 'info'})
subtitle_elements = soup.find_all(name='c-contents-desc', attrs={'slot': 'contents'})

for c_menu_share, date_element, subtitle_element in zip(c_menu_shares, date_elements, subtitle_elements):
    title = c_menu_share.get('data-title')
    href = c_menu_share.get('data-link')
    subtitle = subtitle_element.get_text()
    date = date_element.string

    if title and href:
        제목들.append(title)
        내용들.append(subtitle)
        링크들.append(href)
        날짜들.append(date)

# 다음 페이지부터 처리
page = 2
while True:
    # 페이지 번호에 따라 URL 생성
    if page == 2:
        url = f'https://search.daum.net/search?w=fusion&nil_search=btn&DA=NTB&p={page}&q=%EB%A9%94%ED%83%80%EC%9D%B8%EC%82%AC%EC%9D%B4%ED%8A%B8'
    else:
        url = f'https://search.daum.net/search?w=fusion&nil_search=btn&DA=PGD&p={page}&q=%EB%A9%94%ED%83%80%EC%9D%B8%EC%82%AC%EC%9D%B4%ED%8A%B8'

    # 초기 URL에 접속하여 HTML 문서 가져오기
    response = requests.get(url)
    html_text = response.text
    soup = bs(html_text, 'html.parser')

    # <div id="twcColl">에 대한 정보 출력
    div_twcColl = soup.find('div', id='twcColl')

    # <c-menu-share> 요소들을 모두 찾습니다.
    c_menu_shares = div_twcColl.find_all('c-menu-share')

    date_elements = soup.find_all(name='c-frag', attrs={'slot': 'info'})
    subtitle_elements = soup.find_all(name='c-contents-desc', attrs={'slot': 'contents'})

    for c_menu_share, date_element, subtitle_element in zip(c_menu_shares, date_elements, subtitle_elements):
        title = c_menu_share.get('data-title')
        href = c_menu_share.get('data-link')
        subtitle = subtitle_element.get_text()
        date = date_element.string

        if title and href:
            제목들.append(title)
            내용들.append(subtitle)
            링크들.append(href)
            날짜들.append(date)

    # 페이지 번호 증가
    page += 1

    # 마지막 페이지인 경우 반복문 종료
    if page > 7:
        break

# 수집한 데이터로 DataFrame 생성
데이터 = {
    '제목': 제목들,
    '내용': 내용들,
    '링크': 링크들,
    '날짜': 날짜들
}
df = pd.DataFrame(데이터)

# DataFrame을 Excel 파일로 저장
df.to_excel(r'C:\Users\user\Desktop\search_results.xlsx', index=False)
