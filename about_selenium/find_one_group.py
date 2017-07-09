# -*- coding: utf-8 -*-

from selenium import webdriver
import time

dr = webdriver.Firefox()

file_path = r'file:///D:/TA_Project/library/about_selenium/checkbox.html'

dr.get(file_path)

time.sleep(3)

#checkboxs = dr.find_elements_by_css_selector('input[type=checkbox]')

#checkboxs = dr.find_elements_by_xpath("//div[@class='controls']/input")

#checkboxs = dr.find_elements_by_xpath("//div[@class='controlsp']/input")

checkboxs = dr.find_elements_by_xpath("//input")

for checkbox in checkboxs:
    if checkbox.get_attribute('type') == 'checkbox':
        checkbox.click()

time.sleep(3)

print len(checkboxs)

dr.quit()

