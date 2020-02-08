#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import csv
import time
import requests
from retrying import retry
from lxml import html
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)

etree = html.etree

proxy = {}

# 代理ip地址
proxy_url = ''


@retry(stop_max_attempt_number=3, wait_random_min=1000, wait_random_max=5000)
def change_proxy(retry_count):
    if retry_count < 0:
        return

    result = requests.get(proxy_url).json()
    if result['msg'] == 'ok':
        ip = result['obj'][0]['ip']
        port = result['obj'][0]['port']
        proxies = {"http": "http://" + ip + ":" + port, "https": "http://" + ip + ":" + port}
        global proxy
        proxy = proxies
        print(f"代理ip为更改为：{proxies}")
        return proxies
    else:
        time.sleep(1)
        print('切换代理失败，重新尝试。。。')
        change_proxy(retry_count - 1)


def save_data(filename, data):
    if os.path.isfile(filename):
        is_exist = True
    else:
        is_exist = False
    with open(filename, "a", newline="", encoding="utf_8_sig") as f:
        c = csv.writer(f)
        if not is_exist:
            """need = [user_id, user_name, created_at, source,
                    content, reposts_count, comments_count, attitudes_count,
                    pics_url, video_url, retweeted_status, retweeted_url,
                    topic_num, topics]"""
            c.writerow(['标准号', '标准中文名称', '发布日期', '实施日期', '废止日期', '国际标准分类号', '国际标准分类号前两位'])
        for line in data:
            c.writerow(line)


def spider(page):

    header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Cookie': 'Hm_lvt_3122593ef7de9af6abeec2ee6b2e11a4=1580988241; JSESSIONID=0592A830D0F2317D5B62100A1D2FCC6F; Hm_lpvt_3122593ef7de9af6abeec2ee6b2e11a4=1580991606',
        'Host': 'std.samr.gov.cn',
        'User-Agent': ua.random,
    }

    param = {
        'state': 'G_STATE:现行',
        'sortOrder': 'asc',
        'pageSize': 15,
        'pageNumber': page
    }
    url = 'http://std.samr.gov.cn/gb/search/gbQueryPage'

    def get_ret(c):
        if c < 0:
            return
        try:
            ret = requests.get(url=url, headers=header, params=param, proxies=proxy, timeout=(3, 7)).json()

            return ret
        except:
            change_proxy(3)
            return get_ret(c-1)

    ret = get_ret(3)

    need_list = []

    rows = ret['rows']

    for row in rows:
        try:
            ACT_DATE = row['ACT_DATE']  # 实施日期
        except:
            ACT_DATE = ''
        C_C_NAME = row['C_C_NAME']  # 标准中文名称
        C_STD_CODE = row['C_STD_CODE']  # 标准号
        try:
            ISSUE_DATE = row['ISSUE_DATE']  # 发布日期
        except:
            ISSUE_DATE = ''
        # PROJECT_ID = row['PROJECT_ID']
        # STATE = row['STATE']
        # STD_NATURE = row['STD_NATURE']
        id = row['id']

        detail_url = 'http://std.samr.gov.cn/gb/search/gbDetailed?id=' + str(id)


        def get_detail_ret(c):
            if c < 0:
                return
            try:
                detail_ret = requests.get(url=detail_url, headers=header, proxies=proxy, timeout=(3, 7)).content.decode()
                # print(detail_ret)
                root = etree.HTML(detail_ret)
                content = root.xpath("string(//*)")

                return root
            except:
                change_proxy(3)
                return get_detail_ret(c - 1)

        root = get_detail_ret(3)

        # 废止日期
        abolish_time = root.xpath("//div[@class='events']/ol/li[3]/a/span/text()")[0] \
            if root.xpath("//div[@class='events']/ol/li[3]/a/span/text()") else ''
        abolish_time = abolish_time.replace('\r', '').replace('\t', '').replace('\n', '').replace('于\xa0', '')

        # 国际标准分类号
        hao = root.xpath("//div[@class='basic-info cmn-clearfix'][1]/dl[@class='basicInfo-block basicInfo-right']/dd[2]/span/text()")[0] \
            if root.xpath("//div[@class='basic-info cmn-clearfix'][1]/dl[@class='basicInfo-block basicInfo-right']/dd[2]/span/text()") else ''
        hao2 = hao[0:2]
        need = [C_STD_CODE, C_C_NAME, ISSUE_DATE, ACT_DATE, abolish_time, hao, hao2]

        print(need)
        need_list.append(need)

    return need_list


if __name__ == '__main__':
    for page in range(1498, 1500):
        data = spider(page)
        save_data('现行.csv', data)
        print(f'第{page}页保存成功')
