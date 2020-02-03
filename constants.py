# -*- coding: utf-8 -*-
import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)

# 代理ip地址
proxy_url = 'http://route.xiongmaodaili.com/xiongmao-web/api/glip?secret=4ed5fac7b24bba823e18f5299a16232e&orderNo=GL20200131152126nmVxqyej&count=1&isTxt=0&proxyType=1'

# app
app_url = 'https://m.weibo.cn/api/container/getIndex'

token = '8e4a6f'

app_header = {
    'X-XSRF-TOKEN': token,
    'User-Agent': ua.random,
    'Accept': 'application/json, text/plain, */*',
    'MWeibo-Pwa': '1',
    'Upgrade-Insecure-Requests': '1',
    'X-Requested-With': 'XMLHttpRequest'
}

app_param = {
    'type': 'uid',
    'value': 5745966493,
    'containerid': '1076035745966493',
    'since_id': '4465339964799573'
}

# res = requests.get(url=app_url, headers=app_header, params=app_param).json()
# print(res)
