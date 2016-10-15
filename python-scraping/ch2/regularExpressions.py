from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# 正则
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    print(image)
    print("src="+image["src"])

print("done")