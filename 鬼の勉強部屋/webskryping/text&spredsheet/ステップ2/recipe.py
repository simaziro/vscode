import requests
from bs4 import BeautifulSoup

#spreadsheet秘密鍵とかを連結するやつ
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#spreadsheetのテンプレ
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("py.json",scope)  # type: ignore
gc = gspread.authorize(creds)

#取得したデータを書き出すスプレッドシートのキー
spreadsheetkey = "1dgJHdQ4amKT0p-hHF5I3kG0AsPFobfVWgN1NDE1wBGA"
wb = gc.open_by_key(spreadsheetkey)
ws = wb.worksheet("転職_エンジャパン")#シート名

#spreadsheetに書き込むapped_row　1行に横に入れていく
items = ["No","会社名","給与","勤務地","詳細URL"]
ws.append_row(items,table_range="A1")


#-------------------ここからスクレイピング--------------
# heafers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"}
en_japanURL = "https://employment.en-japan.com"
#スクレイピング対象のURL
URL = "https://employment.en-japan.com/search/search_list/?occupation=400000&areaid=23"
res = requests.get(URL)
soup = BeautifulSoup(res.text,"html.parser")


#HTMLの抽出範囲を決定
jobs = soup.find_all("div",class_="list")

for i , jobs in enumerate(jobs):
  item_companyname = jobs.find("span",class_="company").getText()
  item_money = jobs.select("li",class_="data")[2].getText()
  item_contact = jobs.select("li",class_="data")[3].getText()
  item_url = en_japanURL + jobs.find("a")["href"]
  ws.append_row([i+1,item_companyname,item_money,item_contact,item_url])


