# -*- coding:utf-8 -*-
"""
@Time : 2023/3/24
@Author : skyoceanchen

@TEL: 18916403796
@File : name.py 
@PRODUCT_NAME : PyCharm 
"""


def create_variable_name(num=None, start_with=None, names=[]):
    if names:
        for name in names:
            locals()[name] = None
        return names
    names = []
    if num:
        if not start_with:
            raise Exception()
        for i in range(num):
            locals()[f"{start_with}_{str(i)}"] = None
            names.append(start_with + str(i))
        return names
