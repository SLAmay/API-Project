#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/7/7 16:51
# @Author  : mei
# @File    : baseApi.py
import logging

import requests


class baseApi:
    mobile_host = "http://mobile.ximalaya.com"
    qf_host = "http://qf.ximalaya.com"
    upload_host = "https://cupload.ximalaya.com"
    header = {
        'Cookie': '1&_device=android&15567015-b6b3-311f-8312-d83b72112ebb&9.1.60;1&_token=92954731&A1BEC880340C41E5EEF0E403C3740C820217EB6463930AC6811777FD36C9C011513CE17BCDB5111M55338bb38626DF9_;channel=default;impl=com.ximalaya.ting.android;osversion=29;fp=00811364432322422v64v063196010k220111200100220011101311022040;device_model=VOG-AL00;XIM=;c-oper=%E6%9C%AA%E7%9F%A5;net-mode=WIFI;res=720%2C1510;AID=xsaU+Soxn0o=;manufacturer=HUAWEI;XD=RCXFRkCfVAOsL1Tw8y+iJWP1yqcGvYah75UcNWP3TfMcJK1/0O39iN9IsKEQw+SKdS1vubmCoJHeWVbQs77dA4O/1/C1BBqjzd5T2ic+0SFRvFxBPLW+NALnqg2witEx;umid=681289bb5abd00b248db3a07328e16aeod;xm_grade=0;specialModeStatus=0;oaid=dfff5f7b-7919-fd11-f7f8-bbdfbf97f4a9;newChannelId=yz-huawei;hmVOver3=1;',
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
        "intro": "节目主题：还是觉得基地距离顾客几何级数的解放军节假日绝地反击嫩嫩嫩嫩分局积极投入可可可可可可可解决看看金额渐入佳境日推不过刚刚通过v笨笨笨他爸爸也没看反馈好多好多话和你睡好热好热可可呵呵笨呢嘿嘿嘿可可会很帅气无语喝喝酒渐入佳境天呢合格后会...",
        "introRich": "<br />节目主题：<br /><br />还是觉得基地距离顾客几何级数的解放军节假日绝地反击嫩嫩嫩嫩分局积极投入可可可可可可可解决看看金额渐入佳境日推不过刚刚通过v笨笨笨他爸爸也没看反馈好多好多话和你睡好热好热可可呵呵笨呢嘿嘿嘿可可会很帅气无语喝喝酒渐入佳境天呢合格后会无期可可可解决<br />适合谁听：<br /><br /><br />内容重点：<br /><br /><br />书籍信息：<br /><br /><br />主播寄语：<br /><br /><br />主播介绍：<br /><br /><br />适合人群：<br /><br /><br />更新频率：<br /><br /><br />主播寄语：<br /><br /><br />内容重点：<br /><br /><br />节目主题：<br /><br /><br />内容重点：<br /><br />",
        "isOpenGiftSwitch": 0,
        "customTitle": "卖点",
        "title": "自动化编辑专辑",
        "categoryId": 6,
        "tags": '{"10787":["儿童内容分类"],"11173":["少儿文学"]}'
    }
    create_data = {
        "copyright": "true",
        "albumId": 73054870 ,
        "title": "自动化测试",
        "shareThirdpartyNames": "chaos",
        "type": 0,
        "device": "android",
        "categoryId": 6
    }
    upload_data = {
        "appkey": "tingAndroid",
        "ctxList": [
            "7612de06-6877-4ad3-b3ee-7fdba89a6109",
            "bb877dbd-b832-45a5-ba85-fa730068a9a2",
            "0dd1f740-c112-4b55-bd10-d595809f5052"
        ],
        "deviceType": "android",
        "fileExtName": "m4a",
        "fileName": "5：43的音频.m4a",
        "fileSize": 2776619,
        "multipartId": "TkzvGDFVqDohkrFSkrBYqik4qLDRX-oRkPuITs1t-szLl_RaD8ePOXsfaDWVz8Jsj6lI2e8bk1Hkle2_Yr-wFckBgw-KIwp7v7xdNLHWARnviOgq7Q",
        "uploadType": "tingAndroidAudio"
    }
    update_track_data = {
        "trackId": "655702938",
        "title": "编辑测试",
        "albumId": "73054870",
        "intro": " ",
        "introRich": " ",
        "covers": [{
            "id": 0,
            "crud": "u"
        }],
        "tags": "{\"10747\":[]}",
        "categoryId": "6",
        "visibleCrowdShowType": "2"
    }

    def send(self, method, url, **kwargs):
        request_url = self.xima_host + url
        logging.debug(f'发起的请求的请求地址：=========>{request_url}')
        response = requests.request(method, request_url, **kwargs)
        logging.debug(f'接口的响应信息为：=========>{response.text}')

    # 封装自己的post请求，获取资源
    def post(self):
        pass

    # 封装自己的put请求，获取资源
    def put(self):
        pass

    # 封装自己的delete请求，获取资源
    def delete(self):
        pass




