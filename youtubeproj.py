#!/usr/bin/env python
from pytube import YouTube
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup 
import requests
import os
from AppKit import NSPasteboard, NSStringPboardType
pb = NSPasteboard.generalPasteboard()
pbstring = pb.stringForType_(NSStringPboardType)
linkw=open('youtube-links.txt','w')
abc=pbstring
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
        
        print(video,"Downloading")
    except:
        print("Some Error!")

dir_name = "/Users/Maaz/Downloads/Music"
for f in os.listdir(dir_name):
    r = f.replace(" ","")
    if( r != f):
        os.rename(f,r)

test = os.listdir(dir_name)
for item in test:
    if item.endswith(".webm"):
        cmd=("cd /Users/Maaz/Downloads/Music && ffmpeg -i %s %s.mp3" % (item,item))
        print(cmd)
        os.system(cmd)
        os.remove(os.path.join(dir_name, item))

print('Task Completed!') 
