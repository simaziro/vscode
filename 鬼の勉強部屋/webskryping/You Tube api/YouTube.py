from googleapiclient.discovery import build

import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials



scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("yp.json",scope)  # type: ignore
gc = gspread.authorize(creds)

spreadsheetkey = "1dgJHdQ4amKT0p-hHF5I3kG0AsPFobfVWgN1NDE1wBGA"
wb = gc.open_by_key(spreadsheetkey)
ws = wb.worksheet('シート2')

videoId = 'T4l3Zv3hFfE'
YOUTUBE_API_KEY = "AIzaSyBSPvsf6e-Mxod2Q1u7iNsUwAP7NaXO81w"

keyword = "副業"
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
search_responses = youtube.search().list(
    q=keyword,
    part='snippet',
    type='video',
    regionCode="jp",
    maxResults=20# 5~50まで
).execute()
for search_response in search_responses['items']:
    # snippet
    snippetInfo = search_response['snippet']
    # 動画タイトル
    title = snippetInfo['title']
    # チャンネル名
    channeltitle = snippetInfo['channelTitle']
    
    toto = [title]
    for i in range(1,10):
        ws.update_cell(i+0,2,toto[i-1])


# print(channeltitle)
    # print(title)
    