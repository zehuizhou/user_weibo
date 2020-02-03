#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-02-03 12:16
# @Author  : July
import requests
from lxml import html
import csv


etree = html.etree

url = 'http://www.merida.cn/index.php?m=content&c=index&a=jingxiaoshang&catid=140&types=2'

header = {
    'Host': 'www.merida.cn',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://www.merida.cn/index.php?m=content&c=index&a=jingxiaoshang&catid=237&types=1'
}

def spider():
    ret = requests.get(url=url, headers=header).content.decode()
    root = etree.HTML(ret)
    div_list = root.xpath("//div[@id='show_data']/div")

    print(len(div_list))
    need_list = []
    for div in div_list:
        name = div.xpath(".//h4/a/text()")[0] if div.xpath(".//h4/a/text()") else ''
        phone = div.xpath(".//div[@class='right']/ul/li[1]/text()")[0] if div.xpath(".//div[@class='right']/ul/li[1]/text()") else ''
        place = div.xpath(".//div[@class='right']/ul/li[2]/text()")[0].replace(' ', '') if div.xpath(".//div[@class='right']/ul/li[2]/text()") else ''
        runtime = div.xpath(".//div[@class='right']/ul/li[3]/text()")[0] if div.xpath(".//div[@class='right']/ul/li[3]/text()") else ''
        offtime = div.xpath(".//div[@class='right']/ul/li[4]/text()")[0] if div.xpath(".//div[@class='right']/ul/li[4]/text()") else ''
        need = [name, phone, place, runtime, offtime]
        need_list.append(need)

    return need_list


def save_data(filename, data):
    with open(filename, "a", newline="", encoding="utf_8_sig") as f:
        c = csv.writer(f)
        c.writerow(['店名', '手机号', '地点', '工作日', '休息日'])
        for line in data:
            c.writerow(line)


if __name__ == '__main__':
    data = spider()
    save_data('美利达经销商.csv', data)
