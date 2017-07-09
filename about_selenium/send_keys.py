# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


dr = webdriver.Firefox()

file_path = r'file:///D:/TA_Project/library/about_selenium/send_keys.html'

dr.get(file_path)

#copy content of A

dr.find_element_by_id('A').send_keys(Keys.CONTROL,'a')
dr.find_element_by_id('A').send_keys(Keys.CONTROL,'x')
sleep(3)

#paste to B

dr.find_element_by_id('B').send_keys(Keys.CONTROL,'v')
sleep(3)

#send keys to A

#dr.find_element_by_id('A').send_keys('sun','-','jinguang',Keys.SPACE,'is',Keys.SPACE,'a',Keys.SPACE,'handsome',Keys.SPACE,'boy')
dr.find_element_by_id('A').send_keys('watir', '-', 'webdriver', ' ', 'is', ' ', 'better')  #这里后面直接加空格也可以，keys_space不好用，为啥不好用，还没查清楚
sleep(3)


dr.quit()


