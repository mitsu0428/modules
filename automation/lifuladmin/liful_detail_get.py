import json
import time
import requests
import pandas as pd
from pandas.io.json import json_normalize
access_token = ""

emptyData = []
for x in range(1, 31):
    r = requests.get('https://monthly-api.vacation-stay.jp/v2/admin/inquiries?page={}&per=20'.format(x), 
                    headers={'Content-Type':'application/json','Authorization': 'Bearer {}'.format(access_token)})
    data = r.json()
    for y in data:
            urls = "https://monthly-api.vacation-stay.jp/v2/admin/inquiries/" + y["id"]
            print(urls)
            
            e = requests.get(urls, headers={'Content-Type':'application/json','Authorization': 'Bearer {}'.format(access_token)})
            data2 = e.json()
            
            del data2["room_types"]
            del data2["status"]
            print(data2)
            
            df_json = json_normalize(data2)
            df_json.to_csv('liful_detail.csv', mode='a', encoding="utf-8")
            
            time.sleep(1)

            # print(json.dumps(data2, indent=2, ensure_ascii=False))
            # df = pd.json_normalize(data2)
            # print(df)
 