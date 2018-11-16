#문제 웹데이터-1: python.org 페이지가 가지고 있는 최근 뉴스 출력하기
from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.python.org/").content
soup = BeautifulSoup(html, "html.parser")
def findcrawling():
    all = soup.find("div",{"class":"medium-widget blog-widget"}).find_all("li")
    for item in all:
        a = item.find("a")
        print(a.text)

def selectCrawling():
    all = soup.select("#content > div > section > div.list-widgets.row > div.medium-widget.blog-widget > div > ul > li > a")
    a = [item.text for item in all]
    for i in a:
        print(i)

selectCrawling()


