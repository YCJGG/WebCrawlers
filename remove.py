# _*_coding:utf-8_*_
# Author == zhangjingyi
#Email   == jgg_jingyizhang@foxmail.com


# from pydub import AudioSegment
# import os, re
# from ffmpy import FFmpeg
# # 循环目录下所有文件
# for each in os.listdir('./'):
#     filename = re.findall(r"(.*?)\.mp3", each) # 取出.mp3后缀的文件名
#     #print(filename)
#     if filename:
#         filename[0] += '.mp3'
#         print(filename[0])
#         mp3 = AudioSegment.from_file(filename[0])
#         #mp3 = AudioSegment.from_mp3('./1_雪中悍刀行之西北有雏凤/'+filename[0]) # 打开mp3文件
#         mp3[30*1000:-25*1000].export('./1/'+filename[0]) # 切割前30秒并覆盖保存


import os
import re
import subprocess
import json

current = os.getcwd()
pth = '.\雪中悍刀行\雪中悍刀行'
path = os.listdir(pth)
#print(current)
# path =  r'\1_雪中悍刀行之西北有雏凤'
for chpt in path:
    dirs = os.listdir(current + pth+r'\\'+ chpt )
    #print(dirs)
    for i in dirs:
        if os.path.splitext(i)[1] == '.mp3':
            os.rename(current + pth +r'\\'+ chpt + r'\\' +i,'temp.mp3')
            getmp3 = 'ffmpeg -i temp.mp3'
            result = subprocess.Popen(getmp3,shell=True,stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
            #returnget = subprocess.call(getmp3,shell = True)
            out = result.stdout.read()
            #print(out)
            temp = str(out.decode('utf-8'))
            pattern = re.compile(r'00:\d\d:\d\d')
            data = re.findall(pattern,temp)
            print(data)
            end = data[0].split(':')
            if int(end[2]) < 58:
                end[2] = int(end[2]) + 60 - 58
                end[1] = int(end[1]) - 1
            else:
                end[2] = int(end[2]) - 58
            endtime = str(end[0]) + ':' + str(end[1]) + ':' + str(end[2])

            cutmp3 = 'ffmpeg -i temp.mp3 -ss 00:00:30'+' -to '+endtime+' -acodec copy tempcut.m4a'
            print(cutmp3)
            returncut = subprocess.call(cutmp3,shell = True)
            os.remove('temp.mp3')
            os.rename('tempcut.m4a',os.path.splitext(i)[0] + '.m4a')
    #         #os.rename('temp.mp3',i)
            