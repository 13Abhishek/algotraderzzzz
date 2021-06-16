from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen as uReq
profit_cap=int(input("What is maximum profit do you want to set: "))
loss_cap=int(input("What is maximum Loss do you want to set: "))
number_of_share=int(input("how many shares you would love to buy: "))
change_in_stock_price_for_profit=profit_cap/number_of_share
change_in_stock_price_for_loss=loss_cap/number_of_share
my_url = "https://in.finance.yahoo.com/quote/%5EBSESN?p=%5EBSESN"
uclient = uReq(my_url)
page_html = uclient.read()
page_soup = Soup(page_html, "html.parser")
containers1 = (page_soup.find("span", {"class": "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}))
containers1 = containers1.text
containers1 = containers1.replace(",", "")
containers1 = float(containers1)
current_price = containers1
target_price_profit=current_price+change_in_stock_price_for_profit
target_price_loss=current_price-change_in_stock_price_for_loss
print(current_price)
while True:
        my_url="https://in.finance.yahoo.com/quote/%5EBSESN?p=%5EBSESN"
        uclient=uReq(my_url)
        page_html=uclient.read()
        page_soup=Soup(page_html,"html.parser")
        containers1=(page_soup.find("span",{"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}))
        containers1=containers1.text
        containers1=containers1.replace(",","")
        containers1=float(containers1)
        current_price=containers1

        if current_price>target_price_profit:
         print(current_price)
         print("You made profit")
         break
        if current_price<target_price_loss:
         print(current_price)
         print("you made loss")
         break

