from bs4 import BeautifulSoup as Soup
import requests
from datetime import datetime
from urllib.request import FileHandler, urlopen as uReq
import time
import csv_fileHandler
from csv import writer
from csv import DictWriter
column_name=["Open","Time","High","low","close"]
with open('sample.csv', 'a') as f_object1:
   dictwriter_object = DictWriter(f_object1, fieldnames=column_name)
   dictwriter_object.writeheader()
while True:
    t_end = time.time() + 60 * 1
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    candlestick = {}
    current_price = 0
    MaxPrice = 0
    while time.time()<t_end:
        time.sleep(1)
        my_url="https://in.finance.yahoo.com/quote/%5EBSESN?p=%5EBSESN"
        uclient=uReq(my_url)
        page_html=uclient.read()
        page_soup=Soup(page_html,"html.parser")
        containers1=(page_soup.find("span",{"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}))
        containers1=containers1.text
        containers1=float(containers1.replace(",",""))
        open=containers1
        MinPrice=open
        candlestick["open"]=containers1
        candlestick["Time of opening"]=current_time
        while time.time()<t_end:
            time.sleep(1)
            my_url="https://in.finance.yahoo.com/quote/%5EBSESN?p=%5EBSESN"
            uclient=uReq(my_url)
            page_html=uclient.read()
            page_soup=Soup(page_html,"html.parser")
            containers= page_soup.find_all("div",{"class":"D(ib) Mend(20px)}"})
            containers1=(page_soup.find("span",{"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}))
            containers1=containers1.text
            containers1=containers1.replace(",","")
            containers1=float(containers1)

            # print(f"{containers1} {current_time}")
            current_price=containers1
            if current_price>open:
                MaxPrice=current_price
            else: MaxPrice=open
            if current_price<open:
                MinPrice=current_price
            candlestick["HIGH"]=MaxPrice
            candlestick["LOW"]=MinPrice
        close=current_price
        candlestick["close"]=close
    csv_fileHandler.addRow(["open","Time of opening","HIGH","LOW","close"],candlestick)
    print(candlestick)