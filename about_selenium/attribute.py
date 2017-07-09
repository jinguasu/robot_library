# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep

dr = webdriver.Firefox()
file_path = r'file:///D:/TA_Project/library/about_selenium/attribute.html'
dr.get(file_path)

sleep(2)


element3 = dr.find_element_by_id('tooltip')
print element3.get_attribute('title')