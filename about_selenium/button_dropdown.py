# -*- coding: utf-8 -*-


"""

场景

button dropdown就是把按钮和下拉菜单弄到了一起。处理这种对象的思路一般是先点击这个按钮，等待下拉菜单显示出来，然后使用层级定位方法来获取下拉菜单中的具体项。

代码

下面的代码演示了如何找到watir-webdriver这个菜单项。其处理方法是先点击info按钮，然后等到下拉菜单出现后定位下拉菜单的ul元素，再定位ul元素中link text为watir-webdriver的link，并点击之。
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

dr = webdriver.Firefox()

file_path = r'file:///D:/TA_Project/library/about_selenium/button_dropdown.html'
dr.get(file_path)
sleep(3)
dr.maximize_window()

dr.find_element_by_link_text('Info').click()


#等待点击后出现的框可以用下面的模块
WebDriverWait(dr,10).until(lambda the_driver:the_driver.find_element_by_class_name('dropdown-menu').is_displayed())


menu = dr.find_element_by_link_text('better than')

menu.click()

sleep(3)

dr.quit()




