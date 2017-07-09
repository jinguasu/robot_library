# -*- coding: utf-8 -*-
"""
操作测试对象

click点击对象
send keys在对象上模拟按键输入
clear 清除对象的内容，如果可以的话
"""

from selenium import webdriver
import time

dr = webdriver.Firefox()

file_path = r'file:///D:/TA_Project/library/about_selenium/operate_slement.html'

dr.get(file_path)

#click

dr.find_element_by_link_text('Link1').click()

time.sleep(3)

#send keys
element = dr.find_element_by_name('q')
element.send_keys('something')
time.sleep(3)

#clear
element.clear()
time.sleep(3)

dr.quit()
