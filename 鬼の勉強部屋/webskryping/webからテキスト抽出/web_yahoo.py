from unittest import result
import requests
from bs4 import BeautifulSoup
from pprint import pprint

result = requests.get("https://news.yahoo.co.jp/")
info01 = BeautifulSoup(result.text,"html.parser")
info02 = info01.find_all("div", class_="yjnSub_list_text")


for news in info02:
    pprint(news.getText())