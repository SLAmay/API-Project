#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/8/4 15:57
# @Author  : mei
# @File    : test_search.py
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from businessView.homePage import HomePage
import jsonpath


class TestSaerch(HomePage):

    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'MQS0219619013585'
        desired_caps['appPackage'] = 'com.ximalaya.ting.android'
        desired_caps['appActivity'] = '.host.activity.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def teardown(self):
        self.driver.quit()

    def test_serach(self):
        self.home_page()
        self.search_key('郭德纲')
        result = (MobileBy.XPATH, '//*[@content-desc="郭德纲"]')
        assert result == '郭德纲'
