#!/usr/bin/env python
from pytube import YouTube
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup 
import requests
linkw=open('youtube-links.txt','w')
abc=input('PLEASE ENTER YOURE YOUTUBE PLAYLIST LINK :')
r = requests.get(abc)
page = r.text
soup=BeautifulSoup(page,'html.parser')
res=soup.find_all('a',{'class':'pl-video-title-link'})
for l in res:
    print ('https://youtube.com'+l.get("href",None))
    
    linkw.write('https://youtube.com'+l.get("href",None)+"\n")
linkw.close()
SAVE_PATH = "/Users/Maaz/Downloads/Music" #to_do 
  
link=open('youtube-links.txt','r') 
  
for i in link:
    try:
            
        YT = YouTube(i)
    except:
        print("Connection Error")
    try:
        
        video = YT.streams.filter(only_audio=True, subtype='webm', abr='160kbps').first().download(SAVE_PATH)
    except:
        print("Some Error!")
print('Task Completed!') 