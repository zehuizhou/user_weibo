# -*- coding: utf-8 -*-
import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)

# 代理ip地址
proxy_url = 'http://route.xiongmaodaili.com/xiongmao-web/api/glip?secret=8d7cc3c74eeb76ad422c67df45944d31&orderNo=GL20200131152126nmVxqyej&count=1&isTxt=0&proxyType=1'

# app
app_url = 'https://m.weibo.cn/api/container/getIndex'

token = 'ef54cd'

app_header = {
    'X-XSRF-TOKEN': token,
    'User-Agent': ua.random,
    'Accept': 'application/json, text/plain, */*',
    'MWeibo-Pwa': '1',
    'Upgrade-Insecure-Requests': '1',
    'X-Requested-With': 'XMLHttpRequest',
    'cookie': '_ga=GA1.2.852180565.1582702609; _T_WM=70668980778; ALF=1590283316; WEIBOCN_FROM=1110005030; SCF=AqURd7rrLbKR6K42oMeW_I-_GcEWkVQLrLN_HSe9iIZfKeK1rj9mDtdeFZ0MHp9-u1mpeo1RFUpg-P5uUqyvxIw.; SUB=_2A25zpk8BDeRhGeVI7lER9CvFyD6IHXVRaVFJrDV6PUJbktANLVWnkW1NTAX_rE5oXSCQIHErguXu5B3_WVAzwh8e; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWES-MGSxVJk.S7AzfIp_iT5JpX5K-hUgL.FoecSKe7Sh-4e0z2dJLoIEXLxKBLBonL1h5LxKqL1-BLB-qLxKqLBo5L1KBLxKnLBoBLBKnLxKqLBo5LBoBt; SUHB=0G0euq5tLxxJ7-; SSOLoginState=1587691345; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D1076032803301701%26fid%3D100103type%253D1%2526q%253D%2525E9%252583%252591%2525E7%252588%2525BD%2525E8%2525AF%252584%2525E8%2525AE%2525BA%2525E5%252591%2525A8%2525E6%252589%2525AC%2525E9%25259D%252592%26uicode%3D10000011; XSRF-TOKEN=ef54cd'
}

# res = requests.get(url='https://m.weibo.cn/api/container/getIndex?type=uid&value=1905843503&containerid=1076031905843503&since_id=4482340031788246',
#                    headers=app_header,timeout = 10).json()
# print(res)
