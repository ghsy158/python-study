from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html,'html.parser')
imgLocation = bsObj.find("a", {"id": "logo"}).find("img")["src"]
urlretrieve(imgLocation, "logo.jpg")
