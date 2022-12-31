import os
import gspread
import pandas as pd

from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials


def auth_spreadsheet(key, sheet_name):
    """
    スプレッドシートに接続する関数
    key: スプレッドシートのIDが引数に必要
    sheet_name: 接続したいシートの名前が引数に必要
    """
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    jsonFile = os.path.join(os.path.abspath(os.path.dirname(__file__)), "settings.json")
    credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonFile, scope)
    gc = gspread.authorize(credentials)
    ss_key = key
    worksheet = gc.open_by_key(ss_key).worksheet(sheet_name)
    return worksheet


def count_ss_index(key, sheet_name):
    """
    特定のスプレッドシートの最終行+1行のカウントを返す関数
    key: SpreadsheetのID
    sheet_name: 任意のシート名
    用途例: 
    Pythonで指定行の下に追記していく場合に、set_with_dataframeする際、最終行を指定して書き込む必要がある
    """
    #json 鍵ファイル
    json_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "settings.json")
    worksheet = auth_spreadsheet.auth_spreadsheet(
        json_file, 
        key,
        sheet_name
    )
    #IDの入っている1列目
    worksheet_col = worksheet.col_values(1)
    #行数取得
    worksheet_col_length = len(worksheet_col)
    #最終行+1行の数を返す
    return worksheet_col_length + 1