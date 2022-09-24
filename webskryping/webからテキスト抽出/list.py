import requests
from bs4 import BeautifulSoup
from pprint import pprint


#レシピのスクレイピング

res = requests.get("https://www.orangepage.net/rankings")
soup = BeautifulSoup(res.text,"html.parser")

section = soup.find("div",class_="rankingsList rankingsList--comp")
post_blok = section.find_all("p",class_="tit")

#for n in post_blok:
    #pprint(n.getText())
text = [x.string for x in post_blok]
pprint(text)
