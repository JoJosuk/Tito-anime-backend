# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import pipreqs
url='https://anilist.co/search/anime/trending'
baseurl='https://anilist.co'
def init():
    itempage=requests.get(url)
    itempage=BeautifulSoup(itempage.content,'html.parser')
    itemresults = itempage.find('div', class_='results cover')
    animecards=itemresults.find_all('div',class_='media-card')[:12]
    for animecard in animecards:
        title=animecard.find('a',class_='title').get_text()
        imageurl=animecard.find('img',class_='image')['src']
        urldata=baseurl+animecard.find('a',class_='cover')['href']
        animepage=requests.get(urldata)
        animepage=BeautifulSoup(animepage.content,'html.parser')
        animedata=animepage.find('div',class_='data')
        animeinfo=animedata.find_all('div',class_='data-set')[:10]
        dictaniinfo={}
        for typeinfo in animeinfo:
            type=typeinfo.find('div',class_='type').get_text()
            
            value=typeinfo.find('div',class_='value')
            if value==None:
                if type=='Season':
                    value=typeinfo.find('a').get_text()
                else:
                    value='None'
            else:        
                value=value.get_text()
            type=type.replace('\n',' ')
            value=value.replace('\n',' ')
            
            dictaniinfo[type]=value
        print(dictaniinfo)  
init()