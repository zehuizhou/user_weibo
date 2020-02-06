#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-02-04 17:14
# @Author  : July
import re
import os
import csv
import time
from retrying import retry
from constants import *
from lxml import html

etree = html.etree

proxy = {}

since_id = '4468349641659375'


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
            c.writerow(['用户id', '昵称', '发表时间', '发布设备', '正文', '转发数', '评论数', '点赞数',
                        '图片链接', '视频链接', '是否转发', '转发链接', '话题数', '话题', '微博链接'])
        for line in data:
            c.writerow(line)


def spider():
    global since_id
    app_param = {
        'uid': 3097688767,
        'type': 'uid',
        'value': 3097688767,
        'containerid': '1076033097688767',
        'since_id': since_id
    }

    def get_ret(c):
        if c < 0:
            return
        try:
            ret = requests.get(url=app_url, headers=app_header, params=app_param, proxies=proxy, timeout=(3, 7)).json()
            return ret
        except:
            change_proxy(3)
            return get_ret(c-1)

    ret = get_ret(3)

    since_id = ret['data']['cardlistInfo']['since_id']

    need_list = []
    cards = ret['data']['cards']
    for card in cards:
        if card['card_type'] == 9:
            user_id = card['mblog']['user']['id']  # 用户id
            user_name = card['mblog']['user']['screen_name']  # 用户名称
            created_at = card['mblog']['created_at']  # 发布时间
            source = card['mblog']['source']  # 发布工具

            wb_id = card['mblog']['id']
            wb_url = 'https://m.weibo.cn/detail/' + str(wb_id)

            app_detail_url = 'https://m.weibo.cn/statuses/extend?id=' + str(wb_id)

            def get_detail_ret(c):
                if c < 0:
                    return
                try:
                    detail_ret = requests.get(url=app_detail_url, headers=app_header, proxies=proxy, timeout=(3, 7)).json()
                    return detail_ret
                except:
                    change_proxy(3)
                    return get_ret(c - 1)

            detail_ret = get_detail_ret(2)

            html = detail_ret['data']['longTextContent']  # 正文
            root = etree.HTML(html)
            content = root.xpath("string(//*)")

            reposts_count = detail_ret['data']['reposts_count']  # 转发数
            comments_count = detail_ret['data']['comments_count']  # 评论数
            attitudes_count = detail_ret['data']['attitudes_count']  # 点赞数

            pics_url = ''
            if card['mblog']['pic_num'] != 0:
                pics = card['mblog']['pics']
                for pic in pics:
                    tupian = pic['url']
                    pics_url = pics_url + tupian + os.linesep + '   '  # 图片链接

            try:
                video_url = card['mblog']['page_info']['media_info']['stream_url']  # 视频链接
            except KeyError:
                video_url = ''

            retweeted_status = '否'
            retweeted_url = ''

            if 'retweeted_status' in card['mblog']:
                retweeted_status = '是'
                retweeted_url = 'https://m.weibo.cn/detail/' + str(card['mblog']['retweeted_status']['id'])

            topic_num = int(content.count('#') / 2)  # 话题数
            p = re.compile(r'[#](.*?)[#]', re.S)
            topics = '\n'.join(p.findall(content))  # 话题

            need = [user_id, user_name, created_at, source,
                    content, reposts_count, comments_count, attitudes_count,
                    pics_url, video_url, retweeted_status, retweeted_url,
                    topic_num, topics,
                    wb_url]
            print(need)
            need_list.append(need)

    return need_list


if __name__ == '__main__':
    while True:
        data = spider()
        save_data('微博.csv', data)
        print("🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶")
