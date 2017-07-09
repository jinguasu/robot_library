# -*- coding: utf-8 -*-
"""

对分页来说，我们最感兴趣的是下面几个信息

总共有多少页
当前是第几页
是否可以上一页和下一页
"""

from selenium import webdriver
from time import sleep

dr = webdriver.Firefox()

file_path = r'file:///D:/TA_Project/library/about_selenium/pagination.html'

dr.get(file_path)


#get the number of the pages

pages_num = len(dr.find_elements_by_xpath('//div/ul/li')) - 2

print pages_num

#current_page_num = dr.find_elements_by_xpath("//div/ul/li[@class='active']")[0].text

current_page_num = dr.find_element_by_class_name('active')

# 这里有点区别，讲一下 ， 用xpath获取出来的结果是一个list，所以后面我用了【0】去第一个元素，但是下面这种通过class方式
#来找，就不是一个list，所以可以直接用.text来获取内容

print current_page_num.text

dr.quit()

