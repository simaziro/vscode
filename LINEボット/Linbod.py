import pandas as pd
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#↑取り込んだインポート

def auth():
    SP_CREDENTIAL_FILE = "linbot-355914-51c476ca4ecb.json"
    SP_SCOPE = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
        ]


    SP_SHEET_KEY = "1dgJHdQ4amKT0p-hHF5I3kG0AsPFobfVWgN1NDE1wBGA"
    SP_SHEET = "勤怠管理"#シート名 

    Credentials = ServiceAccountCredentials.from_json_keyfile_name(SP_CREDENTIAL_FILE, SP_SCOPE)
    gc = gspread.authorize(Credentials)

    worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet(SP_SHEET)
    return worksheet
worksheet = auth()
print(worksheet)

