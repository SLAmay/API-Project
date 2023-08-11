#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/7/10 16:09
# @Author  : mei
# @File    : xima_config.py
"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import os

import yaml


class XimaConfig:

    def __init__(self):
        default = os.getenv("env", default="dev")
        self.config = yaml.safe_load(open(f"../config/{default}.yaml"))

    @property
    def base_url(self):
        """
        从环境变量，或者配置文件读取。
        :return:
        """
        return self.config.get(["mobile-xima"])

    @property
    def cookie(self):
        return self.config.get("cookieStr")