import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

import requests
from bs4 import BeautifulSoup
from pprint import pprint



scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("sp.json",scope)  # type: ignore
gc = gspread.authorize(creds)

spreadsheetkey = "1dgJHdQ4amKT0p-hHF5I3kG0AsPFobfVWgN1NDE1wBGA"
wb = gc.open_by_key(spreadsheetkey)
ws = wb.worksheet("シート1")#シート名


# ----------recipe---------
# res = requests.get("https://www.orangepage.net/rankings")
# soup = BeautifulSoup(res.text,"html.parser")

# section = soup.find("div",class_="rankingsList rankingsList--comp")
# post_blok = section.find_all("p",class_="tit")


result = requests.get("https://news.yahoo.co.jp/")
info01 = BeautifulSoup(result.text,"html.parser")
post_blok = info01.find_all("div", class_="yjnSub_list_text")


recepi = []
for n in post_blok:
    recepi.append(n.getText())

for i in range(1,20):
    ws.update_cell(i+0,2,recepi[i-1])

