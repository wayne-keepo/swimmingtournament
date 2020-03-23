import urllib.request
# from bs4 import BeautifulSoup
# https://www.netcracker.com/
while True:
    try:
        url = "http://its-spc.ru/"
        html = urllib.request.urlopen(url).read()
        print("хуй")
        print(str(html, 'utf-8'))
    except Exception as e:
        print(e)
# print(html)

