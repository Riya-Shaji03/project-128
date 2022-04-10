from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

START_URL='https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page=requests.get(START_URL)
soup=bs(page.text,'html.parser')
startable=soup.find_all('table')


temp_list=[]
tablerows=startable[7].find_all('tr')

for tr in tablerows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)
print(temp_list)

starnames=[]
stardistance=[]
starmass=[]
starradius=[]

L=len(temp_list)
print(L)
for i in range(1,L):
    starnames.append(temp_list[i][0])
    stardistance.append(temp_list[i][5])
    starmass.append(temp_list[i][7])
    starradius.append(temp_list[i][8])
df=pd.DataFrame(list(zip(starnames,stardistance,starmass,starradius)),columns=['Brown dwarf','Distance','Mass','Radius'])
df.to_csv('dwarfStars.csv')