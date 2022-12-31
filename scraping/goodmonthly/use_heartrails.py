#HeartRailsAPI : http://express.heartrails.com/api.html
#json_HeartRails : http://express.heartrails.com/api/json?method=getStations
#sample_HeartRails : http://express.heartrails.com/api/json?method=getStations&x=135.0&y=35.0

#From geocodingから緯度経度を取得　→　緯度経度から最寄駅情報の取得
import time
import csv
import json
import pandas as pd
import requests

class json_to_object(dict):
    __getattr__ = dict.get

#HeartRailsのAPIを使用
url = "http://express.heartrails.com/api/json?method=getStations"
address_df = pd.read_excel("----住所・X経度・Y緯度の入ったエクセル----")

#x軸が経度、y軸が緯度
address_address = address_df["住所"].to_list()
address_x = address_df["x"].to_list()
address_y = address_df["y"].to_list()

#最後csv出力前のリスト用
for x, y, z in zip(address_x, address_y, address_address):
    response = requests.get(url, params={
        "x" : x,
        "y" : y
    })
    
    response_json = response.json()
    response_dump = json.dumps(response_json, ensure_ascii=False)
    
    address = json.loads(response_dump, object_hook=json_to_object)
    
    try: #0
        name = address.response.station[0].name
        line = address.response.station[0].line
        distance = address.response.station[0].distance
        xval = address.response.station[0].x
        yval = address.response.station[0].y

    except:
        name = "no data"
        line = "no data"
        distance = "no data"
        xval = "no data"
        yval = "no data"
        
    try: #1
        name_1 = address.response.station[1].name
        line_1 = address.response.station[1].line
        distance_1 = address.response.station[1].distance
        xval_1 = address.response.station[1].x
        yval_1 = address.response.station[1].y

    except:
        name_1 = "no data"
        line_1 = "no data"
        distance_1 = "no data"
        xval_1 = "no data"
        yval_1 = "no data"
        
    try: #2
        name_2 = address.response.station[2].name
        line_2 = address.response.station[2].line
        distance_2 = address.response.station[2].distance
        xval_2 = address.response.station[2].x
        yval_2 = address.response.station[2].y

    except:
        name_2 = "no data"
        line_2 = "no data"
        distance_2 = "no data"
        xval_2 = "no data"
        yval_2 = "no data"
        
    try: #3
        name_3 = address.response.station[3].name
        line_3 = address.response.station[3].line
        distance_3 = address.response.station[3].distance
        xval_3 = address.response.station[3].x
        yval_3 = address.response.station[3].y
        
    except:
        name_3 = "no data"
        line_3 = "no data"
        distance_3 = "no data"
        xval_3 = "no data"
        yval_3 = "no data"
    
    station_list = ([z, name, line, distance, xval, yval, name_1, line_1, distance_1, xval_1, yval_1, name_2, line_2, distance_2, xval_2, yval_2, name_3, line_3, distance_3, xval_3, yval_3])
    
    print("--------------------1", name, line, distance, xval, yval)
    print("--------------------2", name_1, line_1, distance_1, xval_1, yval_1)
    print("--------------------3", name_2, line_2, distance_2, xval_2, yval_2)
    print("--------------------4", name_3, line_3, distance_3, xval_3, yval_3)
    time.sleep(2)
    
    with open('station.csv', 'a', encoding="utf-8") as f:
        writer = csv.writer(f, lineterminator='\n') 
        writer.writerow(station_list)