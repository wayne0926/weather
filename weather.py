#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import ntplib
import datetime
import prettytable as pt
# import os
# import time

# PING_RESULT = 0
# NETWORK_RESULT = 0

# def DisableNetwork():
#     ''' disable network card '''
#     result = os.system(u"netsh interface set interface 以太网 disable")
#     if result == 1:
#         print("disable network card failed")
#     else:
#         print("disable network card successfully")

# def ping():
#     ''' ping 主备网络 '''
#     result = os.system(u"ping restapi.amap.com ")
#     #result = os.system(u"ping www.baidu.com -n 3")
#     if result == 0:
#         print("A网正常")
#     else:
#         print("网络故障")
#     return result
 
 
# if __name__ == '__main__':
#     while True:
#         PING_RESULT = ping()
 
#         if PING_RESULT == 0:
#             time.sleep(20)
#         else:
#             DisableNetwork()
# 位置，天气，时间赋值
# 设置高德API秘钥
p = {'key': '91feef17aa2cd875a61f7520dd30207a'}
# 获取API返回的JSON并取回“status”（是否成功（值为0或1,0表示失败；1表示成功）），然后赋值给“t”
t = requests.get('https://restapi.amap.com/v3/ip', params=p).json()['status']
# 判断t是否不等于“1”（不成功）
if t != '1':
    # 向后传递失败信息（“0”）
    t = '0'
# 若“t”不是“1”（不成功）
else:
    # GET获取API返回的JSON并取回“adcode”（高德位置编码），然后赋值给“pCode”
    pCode = requests.get('https://restapi.amap.com/v3/ip', params=p).json()['adcode']
# 判断是否成功（是否为“1”），若不成功（不等于“1”）
if t == '1':
    # 设置高德API秘钥以及位置编码
    p = {'city': pCode, 'key': '91feef17aa2cd875a61f7520dd30207a', 'extensions': 'base'}
    p1 = {'city': pCode, 'key': '91feef17aa2cd875a61f7520dd30207a', 'extensions': 'all'}
    # GET获取API返回的JSON并取回“city”（城市），然后赋值给“place”
    s = requests.get('https://restapi.amap.com/v3/weather/weatherInfo', params=p).json()
    f = requests.get('https://restapi.amap.com/v3/weather/weatherInfo', params=p1).json()
    city = s['lives'][0]['city']
    # 今日
    dweather = s['lives'][0]['weather']
    dtemp = s['lives'][0]['temperature'] + '℃'
    dwind = s['lives'][0]['windpower']
    dwindd = s['lives'][0]['winddirection']
    # 明日
    tdweather = f['forecasts'][0]['casts'][1]['dayweather']
    tnweather = f['forecasts'][0]['casts'][1]['nightweather']
    tdtemp = f['forecasts'][0]['casts'][1]['daytemp'] + '℃'
    tntemp = f['forecasts'][0]['casts'][1]['nighttemp'] + '℃'
    twind = f['forecasts'][0]['casts'][1]['daywind']
    twindd = f['forecasts'][0]['casts'][1]['daypower']
    # 后天
    hdweather = f['forecasts'][0]['casts'][2]['dayweather']
    hnweather = f['forecasts'][0]['casts'][2]['nightweather']
    hdtemp = f['forecasts'][0]['casts'][2]['daytemp'] + '℃'
    hntemp = f['forecasts'][0]['casts'][2]['nighttemp'] + '℃'
    hwind = f['forecasts'][0]['casts'][2]['daywind']
    hwindd = f['forecasts'][0]['casts'][2]['daypower']
    # 大后天
    dhdweather = f['forecasts'][0]['casts'][3]['dayweather']
    dhnweather = f['forecasts'][0]['casts'][3]['nightweather']
    dhdtemp = f['forecasts'][0]['casts'][3]['daytemp'] + '℃'
    dhntemp = f['forecasts'][0]['casts'][3]['nighttemp'] + '℃'
    dhwind = f['forecasts'][0]['casts'][3]['daywind']
    dhwindd = f['forecasts'][0]['casts'][3]['daypower']
    # 汇入总表
    tb = pt.PrettyTable()
    tb.field_names = ["位置", "时间", "日间天气", "日间温度", "日间风向", "日间风力", "晚间天气", "晚间温度"]
    tb.add_row([city, "今日", dweather, dtemp, dwindd, dwind, '×', '×'])
    tb.add_row([city, "明天", tdweather, tdtemp, twind, twindd, tnweather, tntemp])
    tb.add_row([city, "后天", hdweather, hdtemp, hwind, hwindd, hnweather, hntemp])
    tb.add_row([city, "大后天", dhdweather, dhdtemp, dhwind, dhwindd, dhnweather, dhntemp])
    print(tb)
else:
    print('网络连接错误')
# print("="*100)
# print(f)
# print("="*100)
# print(s)
