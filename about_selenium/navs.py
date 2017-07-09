# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.common.keys import Keys

dr = webdriver.Firefox()

file_path = r'file:///D:/TA_Project/library/about_selenium/navs.html'

dr.get(file_path)

sleep(3)

dr.maximize_window()

dr.find_element_by_link_text('Home').click()

sleep(1)

dr.quit()