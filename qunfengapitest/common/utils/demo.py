#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/8/8 19:29
# @Author  : mei
# @File    : demo.py
def students_grade(grade):
    # 闭包无法修改外部函数的局部变量
    grade = '2'
    print("外函数的年级为", grade)
    def output_students(name, gender):
        grade = '1'
        print("内函数的年级为", grade)
        print(f"霍格沃滋开学啦，学生名称是{name},性别是{gender}，年级是{grade}年级")
    return output_students


students_info = students_grade(3)
students_info('zhizhi', 'female')
students_info('harry', 'male')