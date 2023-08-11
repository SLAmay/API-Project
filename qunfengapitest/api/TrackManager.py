#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/7/19 20:47
# @Author  : mei
# @File    : TrackManager.py
import requests
import jsonpath
from api.baseApi import baseApi


class TrackManager(baseApi):
    # mobile_host = "http://mobile.ximalaya.com"
    # qf_host = "http://qf.ximalaya.com"
    # header = {
    #     'Cookie': '1&_device=android&15567015-b6b3-311f-8312-d83b72112ebb&2.1.6;1&_token=92954731&B34C79D0140C399B1FA22FEBE99618B963F28E8F67953385D711667DB589EDFB7E463FE24B01148M55338bb75CD9ECD_;qf_1_device=android&15567015-b6b3-311f-8312-d83b72112ebb&2.1.6;impl=com.ximalaya.qunfeng;osversion=29;channel=ximalaya;'
    # }
    # album_data = {
    #     "title": "自动化测试",
    #     "categoryId": 6,
    #     "tags": '{"10787":["儿童内容分类"],"11173":["少儿文学"]}'
    # }
    # update_data = {
    #     "coverSmall": "http://imagev2.xmcdn.com/storages/eb9f-audiofreehighqps/48/00/GMCoOSYIhtMKAAvBBQI4EJ_k.jpg!op_type=3&columns=86&rows=86&magick=png",
    #     "albumId": "",
    #     "isPublic": "true",
    #     "customTitle": "卖点",
    #     "title": "自动化编辑专辑",
    #     "categoryId": 6,
    #     "tags": '{"10787":["儿童内容分类"],"11173":["少儿文学"]}'
    # }

    def get_track(self):
        path = '/mobile-user/my/tracks/1691725667200?pageId=1&pageSize=20&queryMode=0'
        return requests.request("get", self.mobile_host + path, headers=self.header)

    def track_form(self):
        path = '/mobile-track-write/upload/trackForm'
        return requests.request("post", self.mobile_host + path, data=self.create_data, headers=self.header)
        # return jsonpath.jsonpath(result.json(), f"$.formId")

    def get_audioid(self):
        path = '/upload/merge/mkfile?ts=1691669665986&uid=92954731'
        return requests.request("post", self.upload_host + path, data=self.upload_data, headers=self.header)
        # return jsonpath.jsonpath(result.json(), f"$.uploadId")

    def create_track(self):
        audio_id = jsonpath.jsonpath(self.get_audioid().json(), f"$.uploadId")[0]
        form_id = jsonpath.jsonpath(self.track_form().json(), f"$.formId")[0]
        track_data = {
            "formId": form_id,
            "audioId": audio_id,
            "visibleCrowdShowType": 2,
            "trackChargeType": 0,
            "categoryId": 6,
            "tags": "测试"
        }
        path = '/album-mobile-writer/api1/upload/album_form'
        return requests.request("post", self.mobile_host + path, data=track_data, headers=self.header)

    def update_track(self):
        path = '/mobile-track-write/upload/track/update'
        return requests.request("post", self.mobile_host + path, data=self.update_track_data, headers=self.header)

    def delete_track(self, track_id):
        path = '/mobile-track-write/track/delete'
        return requests.request("get", self.mobile_host + path, params=track_id, headers=self.header)
track = TrackManager()
track.delete_track('655699312')
