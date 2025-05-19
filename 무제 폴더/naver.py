import requests
from bs4 import BeautifulSoup

keyword = input("검색을 원하는 검색어를 입력하새요 : ")
base_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%BB%A4%ED%94%BC&ackey=" + keyword

req = requests.get(base_url)
html = req.text

soup = BeautifulSoul(html, "html.parser")
results = soup.select(".view_wrap")

for i in results:
    title = i.select.one(".title_link").text
    link = i.select.one(".title_link")["href"]
    print(f"제목 : {title}")
    print(f"링크 : {link}")

    print("---------")