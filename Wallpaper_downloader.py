import requests
import os
import  time
from bs4 import BeautifulSoup
import random
with requests.session() as r:
    search_que=input("Search For Wallpapers")
    search_que_l=search_que.split()
    search_que_s="+".join(search_que)
    if not os.path.exists(f'./{search_que}/'):
        os.makedirs(f'./{search_que}/')
    for i in range(0,10):
        try:
            res=r.get(f"https://wallpaperscraft.com/search/?order=&page={i}&query={search_que_l}&size=")
            soup=BeautifulSoup(res.text,features="html.parser")
            for link in soup.find_all('a',{'class':'wallpapers__link'}):
                wall_s=link.get("href")
                wall_link="https://wallpaperscraft.com"+wall_s
                link_r=r.get(wall_link)
                soup_l=BeautifulSoup(link_r.text,features="html.parser")
                for n in soup_l.find_all('img',{'class':'wallpaper__image'}):
                    time.sleep(2)
                    imgas=n.get('src')
                    img=open(f'./{search_que}/{random.randint(0,999999)}.jpg','wb')
                    img_res=r.get(imgas)
                    img.write(img_res.content)




        except:
            pass