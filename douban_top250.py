import requests
from bs4 import BeautifulSoup
def get_name():
    res =requests.get("https://movie.douban.com/top250")
    soup = BeautifulSoup(res.text,'html.parser')
    targets = soup.find_all('div',class_="hd")
    for each in targets:
        print(each.a.span.text)
print(get_name())
