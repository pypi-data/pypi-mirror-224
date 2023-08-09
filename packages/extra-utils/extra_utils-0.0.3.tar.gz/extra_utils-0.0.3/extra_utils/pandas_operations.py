"""
@Time : 2023/5/29 14:21 
@Author : skyoceanchen
@TEL: 18916403796
@项目：JYairports
@File : pandas_operations.by
@PRODUCT_NAME :PyCharm
"""
import pandas as pd


class PandasOperations(object):
    @staticmethod
    def group(data: list, group_fileds: list, orient="records"):
        """
        :param data:分组数据
        :param group_filed: 分组字段
        orient : str {'dict', 'list', 'series', 'split', 'records', 'index'}
            Determines the type of the values of the dictionary.

            - 'dict' (default) : dict like {column -> {index -> value}}  {'DD001': {'post_construction_settlement': {2: -1.248, 5: -1.664, 8: -2.08, 11: -1.664, },'DD002': {'post_construction_settlement': {2: -1.248, 5: -1.664, 8: -2.08, 11: -1.664, },}
            - 'list' : dict like {column -> [values]} {'DD001': {'post_construction_settlement': [-1.248, -1.664, -2.08, -1.664,]},'DD002': {'post_construction_settlement': [-1.248, -1.664, -2.08, -1.664,]}}
            - 'series' : dict like {column -> Series(values)}
            - 'split' : dict like
              {'index' -> [index], 'columns' -> [columns], 'data' -> [values]}
            - 'records' : list like
              [{column -> value}, ... , {column -> value}]
            - 'index' : dict like {index -> {column -> value}}

            Abbreviations are allowed. `s` indicates `series` and `sp`
            indicates `split`.
        :return:
        """
        # g = pd.DataFrame(data).groupby(['get_time'])
        g = pd.DataFrame(data).groupby([*group_fileds])
        dic = {}
        for k, v in g:
            dic[k] = v.to_dict(orient)
        return dic

    # <editor-fold desc="列最大值所在的行">
    @staticmethod
    def max_columns(data: list, filed, orient):
        pf = pd.DataFrame(data)
        return pf[pf[filed] == pf[filed].max()].to_dict()

    # </editor-fold>

    # <editor-fold desc="列最小值所在的行">
    @staticmethod
    def min_columns(data: list, filed, orient):
        pf = pd.DataFrame(data)
        return pf[pf[filed] == pf[filed].min()].to_dict()
    # </editor-fold>
