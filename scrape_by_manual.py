import requests
from bs4 import BeautifulSoup
import pandas as pd
import ctypes

headers = headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

master_dir = "C:\\Users\\andriawan\\Documents\\My Task\\2023\\RS\\"
link_dir = master_dir + "link\\"
f = open(link_dir + "17maret23.txt", 'r+', encoding='utf-8')
linkProd = [line for line in f.read().splitlines()]
f.close()

# productlinks = ["https://www.ruparupa.com/p/krisbow-helm-las-autodark.html?itm_source=product-last-seen-pdp&itm_campaign=krisbow-helm-las-autodark.html&itm_term=10196895&itm_device=desktop"]
discontinue = []
rs_list = []
for link in linkProd:
    try: 
        r = requests.get(link, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        name = soup.find('h1', class_='fkhPMb').text.strip()
        status = soup.find('div', class_='sc-eHgmQL').text.strip()
        brand = soup.find('dl' , class_='sc-iQKALj').text.strip()


        rs_sku = {
            
            'link': link,
            'name' : name,
            'status' : status,
            'brand' : brand,
            }

        rs_list.append(rs_sku)
        print('Saving: ', rs_sku['brand'])
    except Exception as error :
        discontinue.append(link) 
        
df = pd.DataFrame(rs_list)
dfdisc = pd.DataFrame(discontinue)
# print(discontinue)
# print(df)
df.to_csv("getsatus_17032023_2.csv")
dfdisc.to_csv("list_disc_17032023_2.csv")
ctypes.windll.user32.MessageBoxW(0, "Done Process, Please Check the Result !","Sekilas Info", 0)
