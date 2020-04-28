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
    'cookie': 'ALF=1590628107; _T_WM=98632022946; WEIBOCN_FROM=1110003030; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWES-MGSxVJk.S7AzfIp_iT5JpX5K-hUgL.FoecSKe7Sh-4e0z2dJLoIEXLxKBLBonL1h5LxKqL1-BLB-qLxKqLBo5L1KBLxKnLBoBLBKnLxKqLBo5LBoBt; XSRF-TOKEN=bf5274; MLOGIN=1; SCF=ApTuVIRec5rnYko_9HmLKx8JM1Qd-n8MCEh-QuP9AgxCDxhUHwcdJEs34jAzvqqOHz7QelxMclJY58Yi0KDNALU.; SUB=_2A25zo_KpDeRhGeVI7lER9CvFyD6IHXVRb57hrDV6PUJbktANLRfgkW1NTAX_rCJ1jtpbkHpCEh_LY3fD_FwZIOEl; SUHB=0vJ4bSJonIhYtp; SSOLoginState=1588036345; M_WEIBOCN_PARAMS=fid%3D1076031265357020%26uicode%3D10000011'
}

# res = requests.get(url='https://m.weibo.cn/api/container/getIndex?type=uid&value=1905843503&containerid=1076031905843503&since_id=4482340031788246',
#                    headers=app_header,timeout = 10).json()
# print(res)
