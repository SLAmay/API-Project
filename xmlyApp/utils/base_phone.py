#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/7/6 15:52
# @Author  : mei
# @File    : base_phone.py

import os
import subprocess


def get_android_devices_id():
    cmd = 'adb devices'
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()
    for item in result:
        t = item.decode().split("\t")
        if len(t) >= 2:
            return t[0]


def get_android_devices_version():
    cmd = 'adb shell getprop ro.build.version.release'
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()
    for item in result:
        t = item.decode().split("\t")
        if len(t) >= 2:
            return t[0]

if __name__ == '__main__':
    # result = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE,
    #                           stderr=subprocess.PIPE).stdout.readlines()
    # print(result)
    # get_android_devices_id()
    get_android_devices_version()