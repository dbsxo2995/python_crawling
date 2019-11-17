from bs4 import BeautifulSoup
import requests

date = 20191026
for pagecount in range(1, 3):
    html = requests.get("http://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=100&date=" + str(date) + "&page=" + str(pagecount))
    c = html.content
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("li")

    for item in all:
        for item2 in item.find_all("dl"):
            try:
                title = item2.find("dt",{"class":""}).find("a")
                print(title.text.replace("\t", "").replace("\n", "").replace(",", "").replace('"',"").replace("\r", ""))
            except:
                None
