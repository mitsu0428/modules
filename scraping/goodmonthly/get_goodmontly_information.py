import math
import time
import requests
import lxml
import html5lib
import pandas as pd
from bs4 import BeautifulSoup
from pandas.core.frame import DataFrame

def getPage(url):
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    return BeautifulSoup(response.text, 'html.parser')


def postPage(url, i):
    response = requests.post(
        url,
        headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data={
            'this_page_no': i+1,
            'disp_count': 30,
            'disp_count_upper': 30,
            'cmd': 'NEXT_PAGE',
            'random_number': 558,
        }
    )
    response.encoding = response.apparent_encoding
    return BeautifulSoup(response.text, "html.parser")
    
    
def pageCount(url):
    soup = getPage(url)
    count = int(soup.select('.paging .style01')[0].get_text())
    return math.ceil(count / 30)

url = 'https://www.good-monthly.com/easy/?keyword=%C5%EC%B5%FE%C5%D4'
urlOrigin = "https://www.good-monthly.com"

buildingNumberList = []
for x in range(pageCount(url)):
    soup = postPage(url, x)
    numbers = soup.select("h3 > a")
    time.sleep(1)
    for number in numbers:
        buildingNumber = number.get("href")
        buildingNumberList.append(buildingNumber)
    print(len(buildingNumberList))
        
buildingUrlList = []
for y in buildingNumberList:
    buildingUrl = urlOrigin + y
    buildingUrlList.append(buildingUrl)
    print(buildingUrl)

# css01 = "div#headerInnerLeft > h1"
# css02 = "div#txtArea > dl > dd"
# css03 = "div.line2 > dl > dd"

for z in buildingUrlList:
    soup = getPage(z)
    
    data00 = soup.select("div#headerInnerLeft > h1")
    buildingName = data00[0].get_text()
    
    data01 = soup.select("div#txtArea > dl > dd")
    address = data01[0].get_text().replace('\t', '').replace('\n', '')
    station = data01[1].get_text()
    byCar = data01[2].get_text()
    
    data02 = soup.select("div.line2 > dl > dd")
    type = data02[0].get_text()
    area = data02[1].get_text()
    since = data02[2].get_text()
    capacity = data02[3].get_text()
    bedType = data02[4].get_text()
    parking = data02[5].get_text()
    structure = data02[6].get_text()
    minimumContractDays = data02[7].get_text()
    companys = soup.select_one("div > p > a").get_text()
    
    buildingInformation = [buildingName, z, companys, address, station, byCar, type, area, since, capacity, bedType, parking, structure, minimumContractDays]
    building_df = DataFrame(buildingInformation).T
    building_df.to_csv("building_info.csv", mode='a', header=False, index=False)
    
    table_list = pd.read_html(io=z, attrs= {"class": "priceTable"})
    for table in table_list:
        table_df = DataFrame(table)
        table_df["url"] = z
        table_df.to_csv("table.csv", mode='a', header=False, index=False)
    
    time.sleep(1)
    
    