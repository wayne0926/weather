#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import ntplib
import datetime
import prettytable as pt
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
    # ['lives'][0]['city']
    # GET获取API返回的JSON并取回“weather”（天气（中文提示）），然后赋值给“we”
    # we = requests.get('https://restapi.amap.com/v3/weather/weatherInfo', params=p).json()['lives'][0]['weather']
    # GET获取API返回的JSON并取回“temperature”（温度），然后赋值给“tem”
    # tem = requests.get('https://restapi.amap.com/v3/weather/weatherInfo', params=p).json()['lives'][0]['temperature'] + '℃'
    # 汇总天气（中文提示）与温度，并赋值给“wea”
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
tb = pt.PrettyTable()
tb.field_names = ["位置", "时间", "日间天气", "日间温度", "日间风向", "日间风力", "晚间天气", "晚间温度"]
tb.add_row([city, "今日", dweather, dtemp, dwindd, dwind, '×', '×'])
tb.add_row([city, "明天", tdweather, tdtemp, twind, twindd, tnweather, tntemp])
tb.add_row([city, "后天", 112, 120900, 1714.7, 1, 1, 1])
tb.add_row([city, "大后天", 1357, 205556, 619.5, 1, 1, 1])

print(tb)
# print("="*100)
# print(f)
# print("="*100)
# print(s)
