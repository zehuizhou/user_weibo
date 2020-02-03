#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-02-02 11:09
# @Author  : July
import requests
import csv

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Cookie': 'FSSBBIl1UgzbN7N80S=PBvBW8NGdVVRwnXbGn4vtsFhZLGJdTbseiZPuv7_g4ty609wltwiT6I5rX.O2rUz; JSESSIONID=6E39270006930B334B72B1B3F8FB6873; FSSBBIl1UgzbN7N80T=4xz02fwKCnlJxM26u3FCc1yHlkIKUk_WZRMGg0sf1k0Y0M8WIDZ1HKSZvq_YL4vGOXesvfzLX779JKoWTByQrghTY5Dy.EpeWDbUTcpaO2J6_dJU9jI3JvukV5w88ZH5hAZFkNXnfgNwkqpImd3mkiVCyBgb9Sj0VbIaUvoiDr.Nh7LGe6UKZy6vB1dzCnxBmocemur9fYkwkbYjzFqNYaFwS5Ydeou_5exAZzyTUxcbRV0M3R1JOZuqrJ19lDvr0jAftnv_6tn0LOcSYDfaRNSLGohU8idNO2xIYbD14xMo3vXnZ9FXJvTgt1t7pcUmd6w0VajAQwwSBZrW6ByzfNVwi',
    'Host': 'www.scu.edu.cn',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Referer': 'http://www.scu.edu.cn/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

url = 'http://www.scu.edu.cn/'


def spider():
    ret = requests.get(url=url, headers=header).text
    return ret


def save_data(filename, data):
    with open(filename, "a", newline="", encoding="utf_8_sig") as f:
        c = csv.writer(f)
        c.writerow(['id', '语言讲解标题', '城市', 'mprice', 'price', '月销量', '可用状态', '景点'])
        for line in data:
            c.writerow(line)

if __name__ == '__main__':
    data = spider()
    print(data)
