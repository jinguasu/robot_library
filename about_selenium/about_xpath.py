# -*- coding: utf-8 -*-


from selenium import webdriver
import time


dr = webdriver.Firefox()

file_path = r'file:///D:/TA_Project/library/about_selenium/form.html'

dr.get(file_path)

time.sleep(3)

print dr.find_elements_by_xpath('/html/head/title')

print dr.find_elements_by_xpath('//input')

print dr.find_elements_by_xpath('/html/bady/form/div[1]')

print dr.find_elements_by_xpath('/html/bady/form/div[last()]')

print dr.find_elements_by_xpath('/html/bady/form[input]')



dr.quit()