import requests
from bs4 import BeautifulSoup as bs

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

datelist = []
date_elements = soup.find_all(name='c-frag', attrs={'slot': 'info'})

sub_titlelist = []
sub_title_elements = soup.select('c-contents-desc[slot="contents"]')

for element in date_elements:
    datelist.append(element.string)

for element in sub_title_elements:
    sub_title = ''.join([str(item) for item in element.contents if not isinstance(item, str) or not item.startswith('<b>')])
    sub_titlelist.append(sub_title)

# titles, subtitles, hrefs, dates를 함께 출력
for i, c_menu_share in enumerate(c_menu_shares):
    title = c_menu_share.get('data-title')
    href = c_menu_share.get('data-link')

    if title and href:
        print("제목:", title)
        print("내용:", sub_titlelist[i])
        print("링크:", href)
        print("날짜:", datelist[i])
        print("-"*50)

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

    datelist = []
    date_elements = soup.find_all(name='c-frag', attrs={'slot': 'info'})

    subtitlelist = []
    subtitle_elements = soup.find_all(name='c-contents-desc', attrs={'slot': 'contents'})

    for element in date_elements:
        datelist.append(element.string)

    for sub_element in subtitle_elements:
        subtitle = ''.join([str(item) for item in sub_element.contents if not isinstance(item, str) or not item.startswith('<b>')])
        subtitlelist.append(subtitle)

    # titles, subtitles, hrefs, dates를 함께 출력
    for i, c_menu_share in enumerate(c_menu_shares):
        title = c_menu_share.get('data-title')
        href = c_menu_share.get('data-link')

        if title and href:
            print("제목:", title)
            print("내용:", subtitlelist[i])
            print("링크:", href)
            print("날짜:", datelist[i])
            print("-" * 50)

    # 페이지 번호 증가
    page += 1

    # 마지막 페이지인 경우 반복문 종료
    if page > 7:
        break
