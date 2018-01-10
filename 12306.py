# !/usr/bin/env python
__author__='wangqiang'
import requests

def check():
    response = requests.get('https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-01-11&leftTicketDTO.from_station=DLT&leftTicketDTO.to_station=DUT&purpose_codes=ADULT')
    # print(response.text)
    # print(response.json())
    result = response.json()
    return result['data']['result']
# print(check())

nu = 0
for i in check():
    # print(i)
    tmp_list = i.split('|')
    # print(tmp_list[2:])
    # for n in tmp_list:
    #     print(nu,n)
    #     nu += 1
    # nu = 0
    if tmp_list[29] != '无' and tmp_list[23] != '-':
        print("有票",tmp_list[3])
'''
无座 26
软卧 23
硬座 29
硬卧 28
特等商务座 32
一等座 31
二等座 30
'''
''''
网页结构分析
寻找目标数据
    直接通过源代码
    ajax异步加载
    数据混淆js加密
有控件的网站，一般不爬。
'''
