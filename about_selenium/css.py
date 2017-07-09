# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep

dr = webdriver.Firefox()
file_path = r'file:///D:/TA_Project/library/about_selenium/css.html'
dr.get(file_path)

sleep(2)

link = dr.find_element_by_id('tooltip')
print link.value_of_css_property('color')

print dr.find_element_by_tag_name('h3').value_of_css_property('font')

dr.quit()