# web crawlers
# _*_coding:utf-8_*_
# Author == zhangjingyi
#Email   == jgg_jingyizhang@foxmail.com

'''
下载雪中悍刀行
'''

from bs4 import BeautifulSoup
import os
import urllib.request
import json

album_url_ori = 'http://www.ximalaya.com/2342717/album/2684034/?page='
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

path = '.\雪中悍刀行'
if not os.path.exists(path):
    os.mkdir(path)

pages = 9 # 雪中一共有9页

for i in range(2,pages+1):
    album_url = album_url_ori + str(i)
    req = urllib.request.Request(album_url, headers=header)
    res = urllib.request.urlopen(req)
    soup = BeautifulSoup(res.read().decode('utf-8'),'lxml')
    sounds = soup.findAll('a',{'class': 'title', 'href': True}) 
    print('start download album...page  %s' % i)
    for s in sounds:
        referer = 'http://www.ximalaya.com' + s.attrs['href']
        header_s = {
            'referer': referer,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}   
    #print(s.attrs['href'].split('/'))
        audio_json_url = 'http://www.ximalaya.com/tracks/'+ s.attrs['href'].split(r'/')[-2] + r'.json'
        print(audio_json_url)
        audio_req = urllib.request.Request(audio_json_url, headers=header_s)
        audio_res = urllib.request.urlopen(audio_req)
        audio_json = json.loads(audio_res.read())
        audio_url = audio_json['play_path']
        audio_title = audio_json['title']
        print(audio_title + ' downloading...')
        urllib.request.urlretrieve(
            audio_url, os.path.join(path, audio_title + r'.mp3'))
        print(audio_title + ' downloaded')
    print('%s/9页下载完成' %i)