# -*- coding: utf-8 -*-

"""
场景

button group就是按钮组，将一组按钮排列在一起。处理这种对象的思路一般是先找到button group的包裹(wrapper)div，然后通过层级定位，用index或属性去定位更具体的按钮。

代码

下面的代码演示了如何找到second这个按钮。其处理方法是先找到button group的父div，class为btn-group的div，然后再找到下面所有的div(也就是button)，返回text是second的div

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

dr = webdriver.Firefox()
file_path = r'file:///D:/TA_Project/library/about_selenium/button_group.html'

dr.get(file_path)

sleep(3)

buttons = dr.find_elements_by_xpath("//div[@class='btn']")

for button in buttons:
    if button.text == 'second':
        print 'find the button'


dr.quit()

