#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/8/4 15:15
# @Author  : mei
# @File    : homePage.py

from baseView.baseView import BaseView, MobileBy


class HomePage(BaseView):
    search_loc = (MobileBy.XPATH, '//*[@content-desc="搜索"]')
    search_btn = (MobileBy.ACCESSIBILITY_ID, '搜索')
    search_id = (MobileBy.ID, 'main_home_search_text_switcher')
    agree_btn = (MobileBy.ID, 'host_btn_agree')
    pass_btn = (MobileBy.XPATH, '//*[@content-desc="跳过"]')
    close_btn = (MobileBy.ACCESSIBILITY_ID, '')
    home_btn = (MobileBy.ACCESSIBILITY_ID, '首页')

    def home_page(self):
        if self.get_attribute(self.agree_btn, 'clickable') == 'true':
            self.click(self.agree_btn)
            if self.get_attribute(self.close_btn, 'displayed') == 'true':
                self.click(self.close_btn)
        self.click(self.home_btn)

    def search_key(self, key):
        self.send_keys(self.search_loc, key)
        self.click(self.search_btn)
