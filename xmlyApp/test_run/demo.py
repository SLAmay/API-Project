#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/8/2 19:47
# @Author  : mei
# @File    : demo.py

from appium import webdriver
desired_caps={}
desired_caps['platformName']='Android'
desired_caps['deviceName']='MQS0219619013585'
desired_caps['appPackage']='com.ximalaya.ting.android'
desired_caps['appActivity']='.host.activity.MainActivity'
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

driver.quit()
