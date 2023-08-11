#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/7/10 15:14
# @Author  : mei
# @File    : test_get.py
import requests

class AlbumPage:
    url = "http://mobile.ximalaya.com/mobile-user/my/albums/1688975565411"
    header = {
        'Cookie': '1&_device=android&15567015-b6b3-311f-8312-d83b72112ebb&2.1.6;1&_token=92954731&B34C79D0140C399B1FA22FEBE99618B963F28E8F67953385D711667DB589EDFB7E463FE24B01148M55338bb75CD9ECD_;qf_1_device=android&15567015-b6b3-311f-8312-d83b72112ebb&2.1.6;impl=com.ximalaya.qunfeng;osversion=29;channel=ximalaya;'
    }

    def test_get_album(self):
        r = requests.request("get", self.url, headers=self.header)
        assert r.json()["msg"] == '0'
        print(r.json())

    def test_create_album(self):
        pass

