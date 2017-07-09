# -*- coding: utf-8 -*-

from selenium import webdriver

import os


class BASEWEB(object):

    def __init__(self,web_url,username=None,password=None,logpath=None):
        self.web_url = web_url
        self.username = username
        self.password = password
        if logpath:
            self.logpath = logpath
        else:
            self.logpath = os.curdir()
        

