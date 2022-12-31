#pip install googlemapsでpython環境にgoogleMapApi叩く準備
#GCP(GoogleCloudPlatformに登録してAPIKEYを取得しておく/毎月の無料クレジットで4万件ほど可能??※要検索)
import csv
import time
import googlemaps
import pandas as pd

#pandasで住所一覧の列を作って7000件ほど読み込み
#pandas 以外でもリスト形式のデータを渡せばOK
address_df = pd.read_excel(" ----住所の入ったエクセル---- ")
address_list = address_df[" ----住所欄列名---- "].to_list()

googleapikey = 'ABC123def456ghi789'
googleMap = googlemaps.Client(key=googleapikey)

#緯度・経度・住所をリストにまとめる
lat_lng_list = []
for address in address_list:
    location_from_google = googleMap.geocode(address)

    lat_lng = location_from_google[0]["geometry"]["location"]
    latitude = lat_lng["lat"]
    longitude = lat_lng["lng"]

    time.sleep(1)
    lat_lng_list.append([latitude, longitude, address])

#ファイル書き込み
for write in lat_lng_list:
    with open('lat_lng_geocode.csv', 'a', encoding="utf-8") as f:
        writer = csv.writer(f, lineterminator='\n') 
        writer.writerow(write)