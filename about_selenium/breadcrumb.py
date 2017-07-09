# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep

dr = webdriver.Firefox()
file_path = r'file:///D:/TA_Project/library/about_selenium/breadcrumb.html'
dr.get(file_path)
sleep(1)
anstors = dr.find_element_by_class_name('breadcrumb').find_elements_by_tag_name('a')

for i in anstors:
    print i.text

print dr.find_element_by_class_name('breadcrumb').find_element_by_class_name('active').text


dr.quit()

