# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 15:44
# @Author  : Hexiaolei
# @FileName: excel.py
# @Software: PyCharm

import xlrd
import os
from xlutils.copy import copy
#表头结构  ID ApiName Method Description Input ExpectedOutput ActualOutput Result
add_headers = ['ActualOutput','','Result']
add_params = ['specified','respond','success/failed']
class ExcelClass(object):
    def __init__(self,xl_path):
        """
        excel表格完整路径
        :param xl_path:
        :return:
        """
        self._xl_path = xl_path
        self._op = xlrd.open_workbook(self._xl_path)
        self.apiname_col = int()
        self.method_col = int()
        self.description_col = int()
        self.input_col = int()
        self.expected_output_col = int()
        self.params = list()
        self.values = list()

    # def xl_font(self):
    #     """
    #     字体设置
    #     :return:
    #     """
    #     style = xlwt.XFStyle() # 初始化样式
    #     font = xlwt.Font() # 为样式创建字体
    #     font.name = 'Arial'#字体格式
    #     font.bold = True # 黑体
    #     font.height = 11 #字体大小
    #     style.font = font # 设定样式
    #     return style


    def sheet_read(self,sheetname):
        """
        sheet名
        :param sheetname:
        :return:
        """
        if os.path.splitext(self._xl_path)[-1][1:] != 'xls':
            raise TypeError ('Got an invalid excel extension, must \'.xls\'')
        return self._op.sheet_by_name(sheetname)

    def xl_part(self,sheetname):
        """
        sheet名
        :param sheetname:
        :return:
        """
        sheet = self.sheet_read(sheetname)
        self.params = sheet._cell_values[2]
        headers = sheet._cell_values[1]
        self.values = sheet._cell_values[3:]
        self.id_col = headers.index('ID')
        self.api_name_col = headers.index('ApiName')
        self.method_col = headers.index('Method')
        self.description_col = headers.index('Description')
        self.input_col = headers.index('Input')
        self.expected_output_col = headers.index('ExpectedOutput')
        pass

    def xl_parse(self,sheetname):
        """
        sheet名
        :param sheetname:
        :return:
        """
        kwargs_list = list()
        self.xl_part(sheetname)
        for v in self.values:
            kwargs = dict()
            for i in range(self.input_col,self.expected_output_col):
                key = self.params[i].strip()
                if key and key in ['start_time','end_time'] and isinstance(v[i], float):
                    kwargs[key] = xlrd.xldate.xldate_as_datetime(v[i], 0)
                else:
                    kwargs[key] = v[i]
            temp = {
                    "ID":int(v[self.id_col]),"ApiName":v[self.api_name_col],
                    "Method":v[self.method_col],"params":kwargs,
                    "ExpectedOutput":v[self.expected_output_col]
            }
            kwargs_list.append(temp)
        return kwargs_list

    def xlwt_right(self,sheetname,list):
        """

        :param sheetname:
        :param list: [{'ID':,'ActualOutput':{'specified':,'respond':},'Result':'success/failed'}]
        :return:
        """
        new_workbook = copy(self._op)
        sheet = new_workbook.get_sheet(sheetname)
        actual_output_col = self.expected_output_col+1
        for each in add_headers:
            sheet.write(1,add_headers.index(each)+actual_output_col,each)
        for each in add_params:
            sheet.write(2,add_params.index(each)+actual_output_col,each)
        for each in list:
            keys = each.keys()
            for i in range(len(keys)):
                key = keys[i]
                if key in add_params and key == 'specified':
                    sheet.write(each['ID']+2,add_params.index('specified')+actual_output_col,str(each[key]))
                if key in add_params and key == 'respond':
                    sheet.write(each['ID']+2,add_params.index('respond')+actual_output_col,str(each[key]))
                if key in add_params and key == 'success/failed':
                    sheet.write(each['ID']+2,add_params.index('success_failed')+actual_output_col,str(each[key]))
        new_workbook.save(self._xl_path)
