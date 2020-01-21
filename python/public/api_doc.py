# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 17:35
# @Author  : Hexiaolei
# @FileName: value_type_transfer.py
# @Software: PyCharm

import re

class ApiDocClass(object):
    """
    解析api的doc
    """

    def __init__(self):
        self.async_pattern = re.compile(r'\s*:param\s*async\s*bool')
        self.param_pattern = re.compile(r'\s*param.')
        self.split_pattern = re.compile(r'\s+')


    def params_to_dict(self,list,params_dict):
        """
        分隔一行字符串中两个冒号间的字符串得到入参名字和入参类型
        :param list: 分隔后的列表，list
        :param params_dict: 存放入参和入参类型的字典，dict
        :return: dict
        """
        if len(list) == 3:
            params_dict[list[2]]=list[1]
        return params_dict


    def split_params_str(self,params_str,params_dict):
        """

        :param params_str: doc按照\n\n分隔后的字符串列表，list
        :param params_dict: 存放入参和入参类型的字典，dict
        :return:
        """
        temp1_list = [each for each in params_str if not re.match(self.async_pattern,each) ]
        for each in temp1_list:
            for s in each.split(':'):
                if re.match(self.param_pattern,s):
                    self.params_to_dict(self.split_pattern.split(s),params_dict)
        params_dict['async'] = 'bool'

    def doc_parse(self,api_obj):
        """
        通过api的doc来解析入参和入参格式
        :param api_obj: api实例
        :return: dict
        """
        params_dict= dict()
        doc = api_obj.__doc__
        self.split_params_str(doc.split('\n\n')[2].split('\n'),params_dict)
        return params_dict
