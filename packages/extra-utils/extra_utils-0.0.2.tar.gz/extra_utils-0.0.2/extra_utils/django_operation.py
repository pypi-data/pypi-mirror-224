# -*- coding:utf-8 -*-
"""
@Time : 2023/3/24
@Author : skyoceanchen
@TEL: 18916403796
@File : django_operation.py 
@PRODUCT_NAME : PyCharm 
"""

from django.db import connection
from django.forms.models import model_to_dict as model_dict
from django.contrib.auth.hashers import make_password as mk_password, check_password as ch_password
from django.db.models import Aggregate, CharField
from django.db.models.functions import ExtractMonth, ExtractYear
from django.db.models import Count
from django.contrib import messages
import json
import pandas as pd
from basic_type_operations.str_operation import StringOperation
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# <editor-fold desc="自定义分组函数">
class Concat(Aggregate):
    """ORM用来分组显示其他字段 相当于group_concat"""
    function = 'GROUP_CONCAT'
    template = "%(function)s(%(delimit)s,%(distinct)s %(expressions)s,%(delimit)s ORDER BY %(order_by)s ASC)"

    def __init__(self, expression, distinct=False, delimit="\"'\"", order_by="''", **extra):
        super(Concat, self).__init__(
            expression,
            distinct='DISTINCT ' if distinct else '',
            delimit=delimit,
            order_by=order_by,
            output_field=CharField(),
            **extra)

    """
    list_raw = EarlyWarning.objects.filter() \
    .extra(select={create_time: f"DATE_FORMAT({create_time}, '%%Y-%%m-%%d')"}).values('create_time').annotate(
    all_value1=Concat(create_time)).order_by("-create_time").values_list("all_value1",
                                                                                                  'create_time', 'car',
                                                                                                  )
    """


# </editor-fold>


class DjangoOrmSelectOperation(object):
    # <editor-fold desc="按天分组">
    @staticmethod
    def day_group_count_many(model, date_field="create_time", value=['id', ], data_type=Count, **kwargs, ):
        """
        :param model: 模块
        :param field:
        :param kwargs:
        :return:
        """
        many_kwargs = {}
        for index, v in enumerate(value):
            many_kwargs[v] = data_type(v)
        select = {'day': connection.ops.date_trunc_sql('day', date_field)}
        count_data = model.objects.filter(
            **kwargs,
            # create_time__year=this_year,
            # create_time__month=this_month
        ).extra(
            select=select).values('day').annotate(**many_kwargs)
        count_data = pd.DataFrame(count_data).to_dict("list")
        XAxis = count_data.get('day')
        if not XAxis:
            XAxis = []
        if len(value) == 1:
            YAxis = count_data.get(value[0])
            if not YAxis:
                YAxis = []
            data = {"XAxis": XAxis, "YAxis": YAxis}
        else:
            data = {}
            for index, v in enumerate(value):
                YAxis = count_data.get(v)
                if not YAxis:
                    YAxis = []
                data[v] = {
                    "XAxis": XAxis,
                    "YAxis": YAxis
                }
        return data

    @staticmethod
    def day_group_count_many_other(model, date_field="create_time", group_field="sign", group_field_dic={}, value=[],
                                   data_type=Count, **kwargs, ):
        """
        :param model: 模块
        :param field:
        :param kwargs:
        :return:
        """
        many_kwargs = {}
        for index, v in enumerate(value):
            many_kwargs[v] = data_type(v)
        select = {'day': connection.ops.date_trunc_sql('day', date_field)}
        count_data = model.objects.filter(
            **kwargs,
            # create_time__year=this_year,
            # create_time__month=this_month
        ).extra(
            select=select).values('day', group_field).annotate(**many_kwargs).order_by(date_field)
        count_data_g = pd.DataFrame(count_data).groupby([group_field])
        count_data_dic = {}
        for k, v in count_data_g:
            count_data_dic[k] = v.to_dict("list")
        keys_lis = list(count_data_dic.keys())
        data = {}
        for key in keys_lis:
            XAxis = count_data_dic.get(key).get('day')
            YAxis = count_data_dic.get(key).get(value[0])
            if not XAxis:
                XAxis = []
            if not YAxis:
                YAxis = []
            data[group_field_dic.get(key)] = {
                "XAxis": XAxis,
                "YAxis": YAxis,
            }
        return data

    # </editor-fold>
    # <editor-fold desc="按月分组">
    @staticmethod
    def mouth_group_count_many(model, date_field="create_time", value=['id', ], data_type=Count, **kwargs, ):
        many_kwargs = {}
        for index, v in enumerate(value):
            many_kwargs[v] = data_type(v)
        count_res = model.objects.filter(
            **kwargs
            # create_time__gte=time_ago
        ).annotate(
            year=ExtractYear(date_field),
            month=ExtractMonth(date_field)) \
            .values('year', 'month').order_by('year', 'month').annotate(**many_kwargs)
        # 封装数据格式
        data = {}
        if not count_res:
            if len(value) == 1:
                data = {"XAxis": [], "YAxis": []}
            else:
                for index, v in enumerate(value):
                    data[v] = {
                        "XAxis": [],
                        "YAxis": []
                    }
            return data
        count_data = pd.DataFrame(count_res).to_dict("list")
        year_list = count_data.get("year")
        # print([index for index, month in count_data.get('month')])
        XAxis = ["%s-%s" % (year_list[index], month) for index, month in enumerate(count_data.get('month'))]
        if not XAxis:
            XAxis = []
        if len(value) == 1:
            YAxis = count_data.get(value[0])
            if not YAxis:
                YAxis = []
            data = {"XAxis": XAxis, "YAxis": YAxis}
        else:
            for index, v in enumerate(value):
                YAxis = count_data.get(v)
                if not YAxis:
                    YAxis = []
                data[v] = {
                    "XAxis": XAxis,
                    "YAxis": YAxis
                }

        return data

    @staticmethod
    def mouth_group_count_many_other(model, date_field="create_time", group_field="sign", group_field_dic={}, value=[],
                                     data_type=Count, **kwargs, ):
        """
        :param model: 模块
        :param field:
        :param kwargs:
        :return:
        """
        many_kwargs = {}
        for index, v in enumerate(value):
            many_kwargs[v] = data_type(v)
        select = {'day': connection.ops.date_trunc_sql('day', date_field)}
        count_data = model.objects.filter(
            **kwargs,
            # create_time__year=this_year,
            # create_time__month=this_month
        ).annotate(year=ExtractYear(date_field),
                   month=ExtractMonth(date_field)) \
            .values('year', 'month', group_field).order_by('year', 'month').annotate(**many_kwargs)
        count_data_g = pd.DataFrame(count_data).groupby([group_field])

        count_data_dic = {}
        for k, v in count_data_g:
            count_data_dic[k] = v.to_dict("list")
        keys_lis = list(count_data_dic.keys())
        data = {}
        for key in keys_lis:
            year_list = count_data_dic.get(key).get("year")
            XAxis = ["%s-%s" % (year_list[index], month) for index, month in
                     enumerate(count_data_dic.get(key).get('month'))]
            YAxis = count_data_dic.get(key).get(value[0])
            if not XAxis:
                XAxis = []
            if not YAxis:
                YAxis = []
            data[group_field_dic.get(key)] = {
                # "XAxis": count_data_dic.get(key).get('day'),
                "XAxis": XAxis,
                "YAxis": YAxis
            }
        return data

    # </editor-fold>
    # <editor-fold desc="连接查询-更新">
    @staticmethod
    def connection_select(sql, params):
        """
        :param sql: sql语句
        :param params: 替换参数  (par1,par2)
        :return: 列表
        """
        """
        max()：最大值
        min()：最小值
        avg()：平均值
        sum()：和
        count()：记数
        group_concat()：组内字段拼接，用来查看组内其他字段
        升序：order by 字段名  asc
        降序：order by 字段名 desc
        多个排序条件：order by 字段名 asc,字段名 desc
        限制 limit
        limit 1; 查询一条
        limit 5,3;  # 先偏移5条满足条件的记录，再查询3条
        """
        # 查询
        # 单个分组查询
        # """SELECT id,endMark,createTime,KValue,PCN FROM DynamicStrainometertableFiveFun where createTime>=%s AND createTime<%s GROUP BY endMark ORDER BY createTime;"""
        # 分组查询最大值，最小值，平均值
        # """SELECT location, MAX(desiredValue),AVG(desiredValue) FROM DynamicStrainometertableTwo GROUP BY location ORDER BY -createTime limit 30;""")
        # 分组查询这一组的所有数据
        # """SELECT horizon,group_concat(createTime),group_concat(avgTemValue) FROM ThermometerTableTwo  where createTime>=%s AND createTime<%s  group by horizon""",
        # 更新
        # UPDATE project_device as t SET t.roadsection_id = %s WHERE t.id =%s AND (T.roadsection_id != %s OR T.roadsection_id IS NULL)
        #             """, [int(roader_id), int(device_id), int(roader_id)])
        cursor_thickness = connection.cursor()
        cursor_thickness.execute(
            sql, params)
        data = cursor_thickness.fetchall()
        return data

    # </editor-fold>
    # <editor-fold desc="按照每日时间格式化分组求个数">
    @staticmethod
    def date_group(obj, create_time):
        # '%%Y-%%m-%%d %%H:%%i:%%s'
        return obj.objects.filter() \
            .extra(select={create_time: f"DATE_FORMAT({create_time}, '%%Y-%%m-%%d')"}).values(create_time).annotate(
            num=Count(create_time))

    # </editor-fold>
    # <editor-fold desc="针对一个对象的数据进行json化">
    @staticmethod
    def model_to_dict(obj):
        return model_dict(obj)

    # </editor-fold>
    # <editor-fold desc="创造密码">
    @staticmethod
    def make_password(password):
        pwd = mk_password(password)
        return pwd

    # </editor-fold>
    # <editor-fold desc="核对密码">
    @staticmethod
    def check_password(old_password, password):
        return ch_password(old_password, password)

    # </editor-fold>
    # <editor-fold desc="用户验证-密码">
    @staticmethod
    def user_check_password(user_obj, password):
        return user_obj.check_password(password)

    # </editor-fold>
    # <editor-fold desc="设置-密码">
    @staticmethod
    def user_set_password(user_obj, password):
        return user_obj.set_password(password)

    # </editor-fold>


class DjangoOrmValidateOperation(object):
    # <editor-fold desc="偶数验证">
    @staticmethod
    def validate_even(value):
        print("validate_even", value)
        if value % 2 != 0:
            raise ValidationError(
                _('%(value)s is not an even number'),
                params={'value': value},
            )

    # </editor-fold>
    @staticmethod
    def validate_decimals(value):
        print("validate_decimals", value)
        try:
            return round(float(value), 3)
        except:
            raise ValidationError(
                _('%(value)s is not an integer or a float  number'),
                params={'value': value},
            )

    @staticmethod
    def person_id_validator(value):
        """
        对用户身份证进行自定义验证
        :param value:验证的字段值
        :return:身份格式不正确
        """
        ID_compile = re.compile(r'([A-Za-z](\d{6})\(\d\))|(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X|x)$')
        if not ID_compile.match(value):
            raise ValidationError(u"身份证格式不正确")

    @staticmethod
    def zip_code_validator(value):
        """
        对邮政编码进行自定义验证
        :param value: 验证的字段值
        :return:邮政编码格式不正确
        """
        zip_code = re.compile('^[0-9]\\d{5}$')
        if not zip_code.match(value):
            raise ValidationError(u"邮政编码格式不正确")

    @staticmethod
    def password_validator(value):
        """
        对密码进行自定义验证
        :param value: 验证的字段值
        :return:以字母开头，长度在6~18之间，只能包含字符、数字和下划线
        """
        password = re.compile('^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z_]{8,16}$')
        if not password.match(value):
            raise ValidationError(u'以字母开头，长度在6~18之间，只能包含字符、数字和下划线')

        # models

    # password = models.CharField(validators=[password_validator], max_length=100, verbose_name=u'密码', null=True, blank=True)
    # zip_code = models.CharField(validators=[zip_code_validator], max_length=50, verbose_name=u'邮政编码', null=True, blank=True)


class DjangoMessageOperation(object):
    # 你可以使用add_message()方法创建新的messages或用以下任意一个快捷方法：
    # • success()：当操作成功后显示成功的messages
    # • info()：展示messages
    # • warning()：某些还没有达到失败的程度但已经包含有失败的风险，警报用
    # • error()：操作没有成功或者某些事情失败
    # • debug()：在生产环境中这种messages会移除或者忽略
    # 让我们显示messages给用户。。因为messages框架是被项目全局应用，我们可以在主模板（template）给用户展示messages。
    # 打开base.html模板（template）在id为header的<div>和id为content的<div>之间添加

    # messages框架带有一个上下文环境（context）处理器用来添加一个messages变量给请求的上下文环境（context）。
    # 所以你可以在模板（template）中使用这个变量用来给用户显示当前的messages。
    # 现在，让我们修改edit视图（view）来使用messages框架。编辑应用中的views.py文件，edit视图（view）
    @staticmethod
    def message_error(request, msg):
        messages.error(request, msg)

    @staticmethod
    def message_success(request, msg):
        messages.success(request, msg)

    @staticmethod
    def message_info(request, msg):
        messages.info(request, msg)

    @staticmethod
    def message_warning(request, msg):
        messages.warning(request, msg)

    @staticmethod
    def message_debug(request, msg):
        messages.debug(request, msg)


class DjangoErrorOperation(object):
    @staticmethod
    def django_obj_error(obj):
        print(obj.errors)
        errors_dic = obj.errors.as_json()
        errors_dic: dict = json.loads(errors_dic)
        print(errors_dic, type(errors_dic))
        # password2 = errors_dic.get('password2')[0].get('message')
        # username = errors_dic.get('username')[0].get('message')
        # print(password2, username)
        print(obj.error_class)
        keys = list(errors_dic.keys())
        values = list(errors_dic.values())
        print(keys, values)
        error = str()
        for index, key in enumerate(keys):
            error += key
            error += ':'
            for value in values[index]:
                error += value.get('message')
            error += '\t'
        return error


class DjangoRequestFileOperation(object):
    @staticmethod
    def request_file(request, file_name):
        # 获取到file对象
        # file = request.FILES.get('file')
        # print(request.FILES.get('photo').name)
        # print(chinese_english(request.FILES.get('photo').name))
        if request.FILES.get(file_name):
            request.FILES.get(file_name).name = StringOperation.chinese_english(request.FILES.get(file_name).name)
        # 然后调用二进制对象：
        # file_data = file.read()
        # print(file_data)
        return request


class DjangoSql(object):
    # 执行原生语句，查询所有分组的数据
    @staticmethod
    def cursorsql(sql_select):
        """
        sql_select = '''select number, group_concat(get_time),group_concat(`value`),group_concat(rain_value)
        from gw_waterlevelgauge where runway='%s' and get_time >= '%s' and get_time<= '%s' group by number;''' % (
        runway, date_start, date_end)
        :param sql_select:
        :return:
        """
        cursor = connection.cursor()
        cursor.execute(sql_select)
        lis = cursor.fetchall()
        return lis
