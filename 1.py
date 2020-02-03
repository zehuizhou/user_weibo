#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-02-02 11:58
# @Author  : July

from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://www.scu.edu.cn/')
html=browser.page_source
print(html.encode("utf8"))

