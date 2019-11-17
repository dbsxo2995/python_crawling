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
                contentItem = item2.find("dd")
                content = contentItem.find("span",{"class":"lede"})
                print(content.text.replace("\t", "").replace("\n", "").replace(",", "").replace('"',"").replace("\r", "").replace("…","")[1:len(content.text) + 1])
                print(contentItem.find("span", {"class": "writing"}).text)
                print(contentItem.find("span", {"class": "date"}).text)
            except:
                None
            try:
                imgTag = item2.find("dt", {"class": "photo"}).find("img")
                print(imgTag["src"])
            except:
                print("no image")

