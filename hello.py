dfrom urllib.request import urlopen

html = urlopen("http://www.baidu.com")
print('hello world')
print(html.read())