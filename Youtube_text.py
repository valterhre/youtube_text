from pytube import YouTube
from bs4 import BeautifulSoup
import xml
url=input()
vid=YouTube(url)

soup=BeautifulSoup(vid.captions.get_by_language_code('en').xml_captions, 'xml')

t0=soup.find_all('p')
with open(f'{vid.title[0:10]}.txt', 'w+') as f:
    for k in range( len(t0)):
        t=round((int(t0[k]['t'])/ 1000),2)
        text=t0[k].get_text()
        f.writelines(f'\n{t}\n{text}')
