from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html,"html.parser")
nameList = bsObj.find_all("span",{"class","green"})

print("长度:",len(nameList))
for name in nameList:
    print(name.get_text())