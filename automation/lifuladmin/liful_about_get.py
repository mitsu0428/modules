import time
import json
import requests
import pandas as pd

access_token = "AuthorizationTokenを入れる"

for x in range(1, 62):
    r = requests.get('https://monthly-api.vacation-stay.jp/v2/admin/inquiries?page={}&per=20'.format(x), 
                    headers={'Content-Type':'application/json','Authorization': 'Bearer {}'.format(access_token)})
    data = r.json()
    
    df_json = pd.json_normalize(data)
    print(df_json)
    
    df_json.to_csv('liful_about.csv', mode='a', encoding="utf-8")
    
    time.sleep(1)