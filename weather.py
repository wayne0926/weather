#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者：魏然
# 最后修改时间：2020/10/23
import requests
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
    s = requests.get('https://restapi.amap.com/v3/weather/weatherInfo', params=p).json()['lives'][0]
    f = requests.get('https://restapi.amap.com/v3/weather/weatherInfo', params=p1).json()['forecasts'][0]['casts']
    city = s['city']
    # 今日
    dweather = s['weather']
    dtemp = s['temperature'] + '℃'
    dwind = s['windpower']
    dwindd = s['winddirection']
    # 明日
    tdweather = f[1]['dayweather']
    tnweather = f[1]['nightweather']
    tdtemp = f[1]['daytemp'] + '℃'
    tntemp = f[1]['nighttemp'] + '℃'
    twind = f[1]['daywind']
    twindd = f[1]['daypower']
    # 后天
    hdweather = f[2]['dayweather']
    hnweather = f[2]['nightweather']
    hdtemp = f[2]['daytemp'] + '℃'
    hntemp = f[2]['nighttemp'] + '℃'
    hwind = f[2]['daywind']
    hwindd = f[2]['daypower']
    # 大后天
    dhdweather = f[3]['dayweather']
    dhnweather = f[3]['nightweather']
    dhdtemp = f[3]['daytemp'] + '℃'
    dhntemp = f[3]['nighttemp'] + '℃'
    dhwind = f[3]['daywind']
    dhwindd = f[3]['daypower']
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
