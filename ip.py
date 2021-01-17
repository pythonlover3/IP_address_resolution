import requests
import re
import json
import sys
import os

os.system("title IP解析器")
def getipdata():
    try:
        print('*******************************')
        ip = input("请输入要查询的ip,输入q以退出:")
        if ip == 'q':
            sys.exit()
        print ('正在查询...')
        r = requests.get('http://ip-api.com/json/%s?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query' % ip)
        print('查询的ip:',ip)
        print('经度:',r.json()['lon'])
        print('纬度:',r.json()['lat'])
        print('国家或地区:',r.json()['country'])
        print('城市:',r.json()['city'])
        print('地区:',r.json()['regionName'])
        print('大陆:',r.json()['continent'])
        print('时区:',r.json()['timezone'])
        print('代理:',r.json()['proxy'])
        print('是否托管:',r.json()['hosting'])
        print('ISP:',r.json()['isp'])
        print('组织:',r.json()['org'])
        print('是否移动连接:',r.json()['mobile'])
    except KeyError:
        err=r.json()['message']
        if err=='reserved range':
            print('此ip为保留ip')
        if err=='private range':
            print('此ip为内网ip')
        else:
            print('ip格式错误')

while 1:
    getipdata()
