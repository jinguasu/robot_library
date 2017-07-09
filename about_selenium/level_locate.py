# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

dr = webdriver.Firefox()

file_path = r'file:///D:/TA_Project/library/about_selenium/level_locate.html'

dr.get(file_path)

time.sleep(3)

dr.find_element_by_link_text('Link1').click()


time.sleep(3)

