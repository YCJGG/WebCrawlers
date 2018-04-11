# _*_coding:utf-8_*_
# Author == zhangjingyi
#Email   == jgg_jingyizhang@foxmail.com


from pydub import AudioSegment
import os, re
from ffmpy import FFmpeg
# 循环目录下所有文件
for each in os.listdir('./'):
    filename = re.findall(r"(.*?)\.mp3", each) # 取出.mp3后缀的文件名
    #print(filename)
    if filename:
        filename[0] += '.mp3'
        print(filename[0])
        mp3 = AudioSegment.from_file(filename[0])
        #mp3 = AudioSegment.from_mp3('./1_雪中悍刀行之西北有雏凤/'+filename[0]) # 打开mp3文件
        mp3[30*1000:-25*1000].export('./1/'+filename[0]) # 切割前30秒并覆盖保存