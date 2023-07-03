import requests
import pandas as pd
from bs4 import BeautifulSoup

url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
scrappingpage=requests.get(url)
print(scrappingpage)
# print("akshata")
Soup=BeautifulSoup(scrappingpage.text,"html.parser")
# print(Soup)
startable=Soup.find("table")
# print(startable)
datalist=[]

tablerows=startable.find_all("tr")
# print(tablerows)
for tr in tablerows:
    td=tr.find_all("td")
    # print(td)
    data=[i.text.rstrip()for i in td]
    # print(data)
    datalist.append(data)
starname=[]
stardistance=[]
starmass=[]
starradius=[]    
starluminousity=[]
# print(datalist)
# ['0.000−26.74', 'Sun', '', '0.000015813', 'G2', '1', '1', '1']name=1,distance=3,mass=5,radius=6,luminousity=7
for i in range(1,len(datalist)):
    starname.append(datalist[i][1])
    stardistance.append(datalist[i][3])
    starmass.append(datalist[i][5])
    starradius.append(datalist[i][6])
    starluminousity.append(datalist[i][7])
file=pd.DataFrame(list(zip(starname,stardistance,starmass,starradius,starluminousity)),columns=["starname","stardistance","starmass","starradius","starluminousity"])   
file.to_csv("brightstar.csv") 
# print(len(datalist))

    
