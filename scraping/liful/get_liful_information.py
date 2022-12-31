import csv
import time
import json
import requests
import pandas as pd 
    
liful_data = pd.read_csv("Liful_API_URL.csv")
liful_api_url = liful_data["url"].to_list()

for url in liful_api_url:
    
    #最初のページ　APIなく取得出来てない
    response = requests.get(url)
    vals = json.loads(response.text)

    for val in vals:
        
        id = val["id"]
        capacity = val["capacity"]
        floor_plan_text = val["floor_plan_text"]
        exclusive_area = val["exclusive_area"]
        building_name = val["name"]
        price_30d = val["price_30d"]
        price_30d_ini = val["price_30d_initial_cost"]
        structure = val["building"]["structure"]["long_name"]
        lat = val["building"]["lat"]
        lng = val["building"]["lng"]
        accesses_walk = val["building"]["accesses"][0]["walk_time"]
        accesses_line = val["building"]["accesses"][0]["line"]["name"]
        accesses_station = val["building"]["accesses"][0]["station"]["name"]
        
        #URLは別途作成
        building_url = "https://monthly.homes.jp/room_type_id-" + str(id)

        print(str(id), building_name, building_url, capacity, floor_plan_text, exclusive_area, price_30d, price_30d_ini)
        print(lat, lng, accesses_walk, accesses_line, accesses_station)

        with open("Liful_2021_11_01.csv", mode="a", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([str(id), building_name, capacity, floor_plan_text, exclusive_area, price_30d, price_30d_ini, lat, lng, accesses_line, accesses_station, accesses_walk, building_url])
        
        time.sleep(0.5)