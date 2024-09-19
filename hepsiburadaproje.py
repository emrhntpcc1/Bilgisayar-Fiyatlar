import requests
from bs4 import BeautifulSoup
url = "https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98"
headers = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36"
}
html = requests.get(url,headers=headers).content
soup = BeautifulSoup(html,"html.parser")

liste = soup.find_all("li",{"class":"ioT4Vuc096XRVJSksE8n"})
priceList = soup.find_all("div",{"class":"OOJXkBZkNkyU5n1qXUCg price"})

comp_dict = {}

for name,price in zip(liste,priceList):
    compName = name.a.get("title")
    compPrice = price.text.strip()

    comp_dict[compName] = compPrice

num = 0
for name ,price in comp_dict.items():
    num += 1
    print(f"{num}) Bilgisayar İsmi:<{name}> \nFiyat ==> {price}")