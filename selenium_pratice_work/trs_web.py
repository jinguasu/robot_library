# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import os
import time
import re

class TRSWEB(object):

    def __init__(self,url,username,password):
        self.url = url
        self.username = username
        self.password = password

    def _open_web(self):
        self.dr = webdriver.Firefox()
        if self.url.endswith('/'):
            self.dr.get(self.url + 'protected/index.html')
        else:
            self.dr.get(self.url + '/protected/index.html')


    def _input_login_info(self):
        self.dr.switch_to.frame('login')
        self.dr.find_element_by_id("Username").send_keys(self.username)
        self.dr.find_element_by_id('Password').send_keys(self.password)
        self.dr.find_element_by_id('Validate').click()
        #self.dr.find_element_by_xpath('//center/p').click()
        self.dr.find_element_by_xpath("//input[@type='SUBMIT']").click()

    def _login(self):
        try:
            self._open_web()
            time.sleep(3)
            self._input_login_info()
            self.dr.switch_to_alert().accept()
            time.sleep(5)
            self._get_screenshot()
        except Exception as e:
            self._get_screenshot()
            raise Exception(e)

    def _get_screenshot(self):
        now_time = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        pic_name = now_time + '.png'
        full_pic_name = os.path.join(os.curdir + pic_name)
        self.dr.get_screenshot_as_file(full_pic_name)

    def _logout(self):
        try:
            time.sleep(3)
            self.dr.switch_to.frame('navigation')
            all_links = self.dr.find_elements_by_xpath('//html/body/a')
            for link in all_links:
                if link.get_attribute('title') == 'Logout':
                    link.click()
                    break
            time.sleep(3)   #  等待下一个页面生成，否则它还是在当前的界面里搜索，这个问题应该重视，页面操作跟普通的操作不一样。
            self.dr.switch_to.default_content()  #切换到主网页
            self.dr.switch_to.frame('login')
            self.dr.switch_to.frame('view')
            links = self.dr.find_elements_by_xpath("//form/b/input")
            #links = self.dr.find_elements_by_tag_name('input')
            for link in links:
                if link.get_attribute('type').upper() == 'SUBMIT':
                    link.click()
                    break
        except Exception as e:
            self._get_screenshot()
            raise Exception(e)

    def _make_sure_login_success(self):
        try:
            self._open_web()
            time.sleep(3)
            self._input_login_info()
            alert = self.dr.switch_to_alert().accept()
            time.sleep(3)
            self.dr.switch_to.default_content()
            self.dr.switch_to.frame('login')
            self.dr.switch_to.frame('view')
            text = self.dr.find_element_by_xpath('//body/p/font/b/font')
            print text.text
        except Exception as e:
            self._get_screenshot()
            raise Exception(e)

    def _get_invalid_login_info(self):
        try:
            self._open_web()
            time.sleep(3)
            self._input_login_info()
            alert = self.dr.switch_to_alert()
            info = alert.text
            print info
            time.sleep(3)
            alert.accept()
            return info
        except Exception as e:
            self._get_screenshot()
            raise Exception(e)


    def _operate_ssh_and_rdport(self):
        try:
            self._login()
            self.dr.switch_to.default_content()
            self.dr.switch_to.frame('login')
            self.dr.switch_to.frame('navigation')
            self.dr.find_element_by_xpath('//body/nobr/a[9]').click()
            time.sleep(3)
            self.dr.switch_to.default_content()
            self.dr.switch_to.frame('login')
            self.dr.switch_to.frame('view')
            links = self.dr.find_elements_by_tag_name('input')
            for link in links:
                #   print link.get_attribute('value')
                if link.get_attribute('value') == 'Enable SSH Service':
                    link.click()
                    break
        except Exception as e:
            self._get_screenshot()
            raise Exception(e)

if __name__ == '__main__':
    trs = TRSWEB('https://10.68.179.230','Nemuadmin','nemuuser')
    #trs._login()
    trs._operate_ssh_and_rdport()
    #trs._get_invalid_login_info()
    #trs._get_login_info()
    #trs._make_sure_login_success()
    #trs._logout()


