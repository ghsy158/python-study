from urllib.error import HTTPError
from urllib.request import urlopen

from bs4 import BeautifulSoup

# 异常处理

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),"html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle("http://www.pythonscraping.com/pages/page11.html")
if title is None:
    print("Title could not be found")
else:
    print(title)
