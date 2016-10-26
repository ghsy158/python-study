from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

conn = pymysql.connect(host="172.16.88.187",
                       user='hxerp', password="2wsx3edc",
                       db="test", charset="utf8")
cur = conn.cursor()
cur.execute("USE test")
random.seed(datetime.datetime.now())


def store(title, content):
    cur.execute("insert into pages(title,content) VALUES (\"%s\",\"%s\")", (title, content))
    print("保存数据,title:", title)
    cur.connection.commit()


def getLinks(articleUrl):
    try:
        html = urlopen("http://en.wikipedia.org" + articleUrl)
        bsObj = BeautifulSoup(html, "html.parser")
        title = bsObj.find("h1").get_text()
        content = bsObj.find("div", {"id": "mw-content-text"}).find("p").get_text()
        store(title, content)
        return bsObj.find("div", {"id": "bodyContent"}).findAll("a",
                                                                href=re.compile("^(/wiki/)((?!:).)*$"))
    except AttributeError as e:
        pass


links = getLinks("/wiki/Kevin_Bacon")
try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
        print(newArticle)
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()
