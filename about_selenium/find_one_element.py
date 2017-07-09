# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import os

dr = webdriver.Firefox()

file_path = r'file:///D:/TA_Project/library/some_module/form.html'

dr.get(file_path)

time.sleep(5)

dr.find_element_by_xpath('/html/body/form/div[3]/div/label/input').click()

time.sleep(2)

dr.quit()