import requests
from bs4 import BeautifulSoup as bs

url = 'https://news.daum.net/'

response = requests.get(url)
html = response.text

soup = bs(html, 'html.parser')

headline_articles = soup.select('div.item_issue')

for article in headline_articles:
    title_element = article.select_one('strong > a')
    if title_element:
        title = title_element.get_text().strip()
    else:
        title = '제목 없음'

    article_url = title_element['href']

    article_response = requests.get(article_url)
    article_html = article_response.text

    article_soup = bs(article_html, 'html.parser')

    reporter_element = article_soup.select_one('#mArticle > div.head_view > div.info_view > span:nth-child(1)')
    if reporter_element:
        reporter = reporter_element.get_text().strip()
    else:
        reporter = '기자 정보 없음'

    date_element = article_soup.select_one('span.num_date')
    if date_element:
        date = date_element.get_text().strip()
    else:
        date = '날짜 정보 없음'

    print('제목:', title)
    print('기자:', reporter)
    print('날짜:', date)
    print('-' * 50)
