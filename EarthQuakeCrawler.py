#!/usr/bin/env python3
#! -*- encoding:utf-8 -*-
from bs4 import BeautifulSoup
from subprocess import call #pop-up
import os,hashlib,sys,time,requests

url="https://www.cwb.gov.tw/V8/C/E/MOD/EQ_ROW.html?T=2021062318-3"#解析後發現的真實資料位置

md5File=os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])),"Hexdigest_md5.txt")
logFile=os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])),"log.txt")

def GetDATA(key="1"):#LATEST
    #獲取信息
    data=sp.select_one("#eq-"+key)
    id=data.td.text
    level=data.find("td",{"class":"eq_lv-"+key}).text
    time=data.span.text.split("NEW")[0]
    detail=[]#[place,depth,scale] str
    for i in range(3):
        if i<2:
            detail.append(data.select("li")[i].text[2:])
        else:
            detail.append(data.select("li")[i].text[4:])
    return [id,time,level,detail]

while True:
    html=requests.get(url).text.encode("utf-8")#重新請求原始碼
    sp=BeautifulSoup(html,"html.parser")#解析
    new_md5=hashlib.md5(html).hexdigest()#加密算法

    f1=open(md5File,mode="a+")#md5File
    f2=open(logFile,mode="a",encoding="utf-8")#logFile
    f1.seek(0)#因為appending mode 默認的指針在EOF，所以要重置
    old_md5=f1.readline()

    if old_md5!=(new_md5+"\n"):#資料已更新
        f1.seek(0)
        f1.write(new_md5+"\n")
        result=GetDATA()#獲取資料
        #彈窗
        cmd = 'display notification \"' +result[3][0].split("(")[0]\
            +"  規模："+result[3][2]+ '\" with title \"' +result[2]+\
            "地震"+"\t\t\t   "+result[1]+ '\"'
        call(["osascript", "-e", cmd])

        #記錄log
        log=result[2]+"地震"+"    "+result[1]+"    "+result[3][0].split("(")[0]+"    規模："+result[3][2]
        print(log)#終端
        f2.write("["+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"]資料更新："+log+"\n")
        f2.close()
    f1.close()
    time.sleep(60)
