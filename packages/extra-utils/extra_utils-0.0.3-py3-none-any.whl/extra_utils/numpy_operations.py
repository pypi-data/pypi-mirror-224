"""
@Time : 2023/7/17 14:47 
@Author : skyoceanchen
@TEL: 18916403796
@项目：smartAirports
@File : numpy_operations.by
@PRODUCT_NAME :PyCharm
"""
import numpy as np


# <editor-fold desc="numpy矩阵计算方法">
class NumpyOperations(object):
    # <editor-fold desc="二维数组差集">
    @staticmethod
    def calArray2dDiff(array_0, array_1):
        if array_0.any() and array_1.any():
            array_0_rows = array_0.view([("", array_0.dtype)] * array_0.shape[1])
            array_1_rows = array_1.view([("", array_1.dtype)] * array_1.shape[1])
            return (
                np.setdiff1d(array_0_rows, array_1_rows)
                    .view(array_0.dtype)
                    .reshape(-1, array_0.shape[1])
            )
        elif array_0.any():
            return array_0
        elif array_1.any():
            return array_1
        else:
            return []

    # </editor-fold>
    # <editor-fold desc="交集">
    @staticmethod
    def calArray2Intersect1d(array_0, array_1):
        if array_0.any() and array_1.any():
            array_0_rows = array_0.view([("", array_0.dtype)] * array_0.shape[1])
            array_1_rows = array_1.view([("", array_1.dtype)] * array_1.shape[1])
            return (
                np.intersect1d(array_0_rows, array_1_rows)
                    .view(array_0.ddatatype)
                    .reshape(-1, array_0.shape[1])
            )
        elif array_0.any():
            return array_0
        elif array_1.any():
            return array_1
        else:
            return []

    # </editor-fold>
    # <editor-fold desc="并集合">
    @staticmethod
    def calArray2Union1d(array_0, array_1):
        if array_0.any() and array_1.any():
            array_0_rows = array_0.view([("", array_0.dtype)] * array_0.shape[1])
            array_1_rows = array_1.view([("", array_1.dtype)] * array_1.shape[1])
            return (
                np.union1d(array_0_rows, array_1_rows)
                    .view(array_0.ddatatype)
                    .reshape(-1, array_0.shape[1])
            )
        elif array_0.any():
            return array_0
        elif array_1.any():
            return array_1
        else:
            return []
    # </editor-fold>

# </editor-fold>
