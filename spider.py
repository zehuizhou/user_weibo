#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-02-01 08:45
# @Author  : July
import requests
import re
import time
import requests
from lxml import html
import os
import datetime
import string
from retrying import retry
from constants import *
import pysnooper
import sys
import csv

etree = html.etree


def spider(page):
    para = {
        'ajwvr': 6,
        'domain': 100505,
        'is_all': 1,
        'stat_date': '201901',
        'page': page,
        'pagebar': page,
        'pl_name': 'Pl_Official_MyProfileFeed__20',
        'id': 1005055745966493,
        'script_uri': '/A0708008',
        'feed_type': 0,
        'pre_page': page,
        'domain_op': 100505,
        '__rnd': 1580518664258
    }
    res = requests.get(url=start_url, headers=web_header, params=param).json()
    root_html = etree.HTML(res['data'])
    div_list = root_html.xpath("//div")
    print(len(div_list))
    for div in div_list:
        content = div.xpath("string(.//div[@node-type='feed_list_content'])").replace(' ', '')
        tm = div.xpath(".//a[@node-type='feed_list_item_date']/@title")[0]
        print(content)
        print(tm)




if __name__ == '__main__':
    spider(3)