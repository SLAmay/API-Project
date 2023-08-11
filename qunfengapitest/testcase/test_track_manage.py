#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/7/20 16:43
# @Author  : mei
# @File    : test_track_manage.py

import allure

from api.TrackManager import TrackManager
import jsonpath

from utils.log_utils import logger


class TestTrackManager:
    def setup_class(self):
        self.track = TrackManager()

    def test_get_track(self):
        r= self.track.get_audioid()
        logger.info(r.json())
        formid = jsonpath.jsonpath(r.json(), f"$.uploadId")[0]
        logger.info(formid)

    def test_create_track(self):
        """创建声音"""
        # 创建声音成功，查询列表校验
        r = self.track.create_track()
        logger.info(r.json())

    def test_edit_album(self):
        """编辑声音"""
        r = self.track.update_track()
        logger.info(r.json())
        update_title = self.track.update_track_data['title']
        # 获取声音列表
        getTrack = self.track.get_track()
        track_title = jsonpath.jsonpath(getTrack.json(), f"$..list.['title']")
        logger.info(f'获取声音列表声音名称：{track_title}')
        assert r.status_code == 200
        assert (update_title in track_title), "声音编辑失败"

    def test_delete_album(self):
        """删除专辑"""
        # 获取要删除的声音ID
        del_track_id = jsonpath.jsonpath(self.track.get_track().json(), f"$..list.['trackId']")[0]
        logger.info(f"要删除的声音ID为：{del_track_id}")
        r = self.track.delete_track('{del_track_id}')
        # 获取声音列表信息
        getTrack = self.track.get_track()
        track_id = jsonpath.jsonpath(getTrack.json(), f"$..list.['trackId']")
        logger.info(f'获取声音列表声音ID：{track_id}')
        assert r.status_code == 200
        assert (del_track_id not in track_id), "声音删除失败"

