#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/7/7 16:42
# @Author  : mei


# @File    : test_album_manager.py
import allure

from api.AlbumManager import AlbumManager
import jsonpath

from utils.log_utils import logger


class TestAlbumManager:
    def setup_class(self):
        self.album = AlbumManager()

    @allure.description("用例描述")
    @allure.severity("critical，用例等级")
    @allure.feature('测试功能_demo1')
    @allure.story('测试模块_demo2')
    @allure.issue("http://teambition.ximalaya.com/task/5e991d3bdbc10f001")
    @allure.testcase("用例名：xxxx")
    @allure.title("这是title")
    def test_create_album(self):
        """创建专辑"""
        # 创建专辑成功，查询列表校验
        r = self.album.create_album()
        logger.info(r.json())
        create_album_id = jsonpath.jsonpath(r.json(), f"$.albumId")[0]
        logger.info(f'新增专辑的专辑ID:{create_album_id}')
        create_album_title = jsonpath.jsonpath(r.json(), f"$.title")[0]
        logger.info(f"新增专辑的专辑标题：{create_album_title}")

        # 获取列表接口
        getAlbum = self.album.get_album()
        list_id = jsonpath.jsonpath(getAlbum.json(), f"$..list.['albumId']")
        logger.info(f'获取专辑列表专辑ID:{list_id}')
        album_title = jsonpath.jsonpath(getAlbum.json(), f"$..list.['title']")
        logger.info(f'获取专辑列表专辑名称：{album_title}')

        # 校验新增成功
        assert r.status_code == 200
        assert (create_album_id in list_id), "专辑创建失败"
        assert (create_album_title in album_title), "专辑创建失败"

        # 清除创建的专辑数据
        self.album.delete_album(create_album_id)

    def test_edit_album(self):
        """编辑专辑"""
        r = self.album.update_album()
        logger.info(r.json())
        update_title = self.album.update_data['title']
        # 获取专辑列表
        getAlbum = self.album.get_album()
        album_title = jsonpath.jsonpath(getAlbum.json(), f"$..list.['title']")
        logger.info(f'获取专辑列表专辑名称：{album_title}')
        assert r.status_code == 200
        assert (update_title in album_title), "专辑编辑失败"

    def test_delete_album(self):
        """删除专辑"""
        # 删除专辑，获取要删除的专辑ID
        r = self.album.create_album()
        delete_album_id = jsonpath.jsonpath(r.json(), f"$.albumId")[0]
        logger.info(f"要删除的专辑ID为：{delete_album_id}")
        self.album.delete_album(delete_album_id)
        # 获取专辑列表信息
        getAlbum = self.album.get_album()
        album_id = jsonpath.jsonpath(getAlbum.json(), f"$..list.['albumId']")
        logger.info(f'获取专辑列表专辑ID：{album_id}')
        assert r.status_code == 200
        assert (delete_album_id not in album_id), "专辑删除失败"

    def test_get_album(self):
        r = self.album.get_album()
        logger.info(f"获取专辑列表接口响应为：{r.json()}")
        logger.info(f"接口响应码：{r.status_code}")
        assert r.status_code == 200
        # 响应值的提取。
        list_result = jsonpath.jsonpath(r.json(), f"$..list[0]['albumId']")[0]
        logger.info(f'获取专辑列表第一张专辑ID:{list_result}')
        update_title = jsonpath.jsonpath(r.json(), f"$..list[0]['title']")[0]
        logger.info(f'获取专辑列表第一张专辑名称：{update_title}')
        r2 = jsonpath.jsonpath(r.json(), f"$.ret")[0]
        logger.info(r2)
        # 断言创建接口响应信息为正确
        assert r2 == 0
        # 断言更新的专辑名称为正确的
        # assert update_title["title"] == "测试"
