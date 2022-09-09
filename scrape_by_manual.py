from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

rsl=[]
rsl2=[]

urls = ['https://www.monotaro.id/s028337539.html','https://www.monotaro.id/s028337508.html','https://www.monotaro.id/s022659385.html','https://www.monotaro.id/s022659392.html',
        'https://www.monotaro.id/s022659408.html']
#scrape elements
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    span = soup.find("span", class_= "price")
    rsl.append(span.get_text())

    h1 = soup.find("h1", class_= "page-title")
    rsl2.append(h1.get_text())


df=pd.DataFrame([rsl,rsl2])
transRslt=(np.transpose(df))
df_rslt=pd.DataFrame(transRslt)
df_rslt.columns=["price","prod name"]
print(df_rslt)
