#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/7/7 16:31
# @Author  : mei
# @File    : AlbumManager.py
import requests

from api.baseApi import baseApi


class AlbumManager(baseApi):
    # def __init__(self, url):
    #     baseApi.__init__(self, url)
    def setup_class(self):
        self.base = baseApi()

    mobile_host = "http://mobile.ximalaya.com"
    qf_host = "http://qf.ximalaya.com"
    header = {
        'Cookie': '1&_device=android&15567015-b6b3-311f-8312-d83b72112ebb&2.1.6;1&_token=92954731&734F4CD0140C71CB96C63DD595146702280E67421EBB5F49238F583EFAC41BFB1BEACA55EFBC86M55338bb5F08ACF9_;qf_1_device=android&15567015-b6b3-311f-8312-d83b72112ebb&2.1.6;impl=com.ximalaya.qunfeng;osversion=29;channel=ximalaya;',
        'User-Agent': 'okhttp/3.12.1',
        'content-type': 'application/x-www-form-urlencoded'
    }
    album_data = {
        "title": "自动化测试",
        "categoryId": 6,
        "tags": '{"10787":["儿童内容分类"],"11173":["少儿文学"]}'
    }
    update_data = {
        "aiDoc": 0,
        "albumId": "73054870",
        "intro":"节目主题：还是觉得基地距离顾客几何级数的解放军节假日绝地反击嫩嫩嫩嫩分局积极投入可可可可可可可解决看看金额渐入佳境日推不过刚刚通过v笨笨笨他爸爸也没看反馈好多好多话和你睡好热好热可可呵呵笨呢嘿嘿嘿可可会很帅气无语喝喝酒渐入佳境天呢合格后会...",
        "introRich": "<br />节目主题：<br /><br />还是觉得基地距离顾客几何级数的解放军节假日绝地反击嫩嫩嫩嫩分局积极投入可可可可可可可解决看看金额渐入佳境日推不过刚刚通过v笨笨笨他爸爸也没看反馈好多好多话和你睡好热好热可可呵呵笨呢嘿嘿嘿可可会很帅气无语喝喝酒渐入佳境天呢合格后会无期可可可解决<br />适合谁听：<br /><br /><br />内容重点：<br /><br /><br />书籍信息：<br /><br /><br />主播寄语：<br /><br /><br />主播介绍：<br /><br /><br />适合人群：<br /><br /><br />更新频率：<br /><br /><br />主播寄语：<br /><br /><br />内容重点：<br /><br /><br />节目主题：<br /><br /><br />内容重点：<br /><br />",
        "isOpenGiftSwitch": 0,
        "customTitle": "卖点",
        "title": "自动化编辑专辑",
        "categoryId": 6,
        "tags": '{"10787":["儿童内容分类"],"11173":["少儿文学"]}'
    }

    def get_album(self):
        path = '/mobile-user/my/albums/ts-1690024252678'
        return requests.request("get", self.mobile_host+path, headers=self.header)

    def create_album(self):
        path = '/album-mobile-writer/api1/upload/album_form'
        return requests.request("post", self.mobile_host+path, data=self.album_data, headers=self.header)

    def edit_album_detail(self, albumId):
        path = '/album-mobile-writer/studio/album/forEdit'
        return requests.request("get", self.mobile_host+path, params=albumId)

    def update_album(self):
        path = '/mobile/studio/album/update'
        return requests.request("post", self.mobile_host+path, data=self.update_data, headers=self.header)

    def delete_album(self, albumId):
        path = '/mobile/studio/album/delete'
        album_data = {"albumId": albumId}
        return requests.request("post", self.mobile_host+path, data=album_data, headers=self.header)

    def album_detail(self, album_id):
        path = '/api/album/details/ts-1689769987661'
        return requests.request("get", self.qf_host+path, params=album_id)



