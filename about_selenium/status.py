# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep

dr = webdriver.Firefox()
file_path = r'file:///D:/TA_Project/library/about_selenium/status.html'
dr.get(file_path)

sleep(2)

text_filed = dr.find_element_by_name('user')
print text_filed.is_enabled()

print dr.find_element_by_class_name('btn').is_enabled()


radio = dr.find_element_by_name('radio')
radio.click()
print radio.is_selected()

try:
    dr.find_element_by_id('none')
except:
    print 'this element is not exist'

dr.quit()