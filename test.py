# -*- coding: utf-8 -*-
import csv
import random
import time
import os
import sys
import requests
from lxml import html
from constants import proxy_url
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
url = 'http://data.eastmoney.com/gdfx/stock/000882.html'
header = {
    'x-requested-with': 'XMLHttpRequest',
    'host': 'data.eastmoney.com',
    'mweibo-pwa': '1',
    'x-xsrf-token': '3360ad',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'cookie': 'dRecords=%u80A1%u4E1C%u5206%u6790-%u534E%u8054%u80A1%u4EFD%7Chttp%3A//data.eastmoney.com/gdfx/stock/000882.html; qgqp_b_id=5140f63082888acd5f99f5fdf2785475; st_si=70627884296358; st_sn=1; st_psi=20200309135013393-113300301596-9311493896; st_asi=delete; st_pvi=18762100240323; st_sp=2020-03-09%2013%3A50%3A14; st_inirUrl=',
    'accept': 'application/json, text/plain, */*',
    'Referer': 'https://m.weibo.cn/status/IscD7sd2K',
    'User-Agent':  ua.random,
}

ret = requests.get(url=url, headers=header).content.decode('gbk')

print(ret)