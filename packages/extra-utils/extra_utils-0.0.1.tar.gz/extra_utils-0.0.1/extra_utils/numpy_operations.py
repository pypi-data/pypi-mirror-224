"""
@Time : 2023/7/17 14:47 
@Author : skyoceanchen
@TEL: 18916403796
@项目：smartAirports
@File : numpy_operations.by
@PRODUCT_NAME :PyCharm
"""
import numpy as np


class NumpyBase(object):
    # <editor-fold desc="随机创建二维矩阵">
    @staticmethod
    def twomatrix(low, high, size_row, size_col, integer=False):
        """

        :param low:矩阵最小值
        :param high: 矩阵最大值，并都小于最大值
        :param size_row: 行
        :param size_col: 列
        :return:
        """
        # 不包含最大值
        # rand = np.random.randint(low=low, high=high, size=(size_row, size_col))
        # 包含最大值
        # rand = np.random.random_integers(low=low, high=high,  size=(size_row, size_col))
        # 随机小数
        if integer:
            rand = np.random.randint(low=low, high=high, size=(size_row, size_col))
        else:
            rand = np.random.uniform(low=low, high=high, size=(size_row, size_col))
        # print(rand)
        # print(rand.tolist())
        return rand

    # </editor-fold>
    # <editor-fold desc="随机创建三维矩阵">
    @staticmethod
    def threematrix(low, high, size_row, size_col, size_high, integer=False):
        """
        :param low:矩阵最小值
        :param high: 矩阵最大值，并都小于最大值
        :param size_row: 行
        :param size_col: 列
        :param size_high: 高
        :return:
        在size_row个二维  二维内又size_col个一维，一维数组内size_high个数据
        """
        # 不包含最大值
        # rand = np.random.randint(low=low, high=high, size=(size_row, size_col, size_high))
        # 包含最大值
        # rand = np.random.random_integers(low=low, high=high, size=(size_row, size_col, size_high))
        # 随机小数
        if integer:
            rand = np.random.randint(low=low, high=high, size=(size_row, size_col, size_high))
        else:
            rand = np.random.uniform(low=low, high=high, size=(size_row, size_col, size_high))
        # print(rand.tolist())
        return rand

    # </editor-fold>


# <editor-fold desc="numpy矩阵计算方法">
class NumpyOperations(NumpyBase):
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
