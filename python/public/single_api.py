# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 15:52
# @Author  : Hexiaolei
# @FileName: filter_single_api.py
# @Software: PyCharm
from swagger_client.rest import ApiException
from public.api_doc import ApiDocClass
class FilterSingle(ApiDocClass):
    def __init__(self):
        ApiDocClass.__init__(self)

    def single_api(self,params,current_api,api_obj):
        """
        只执行本api方法的用例
        :param params: 转换格式前的所有入参，list
        :param current_api: 当前调用的api实例的名字，str
        :param api_obj: api实例，object
        :return:list
        """
        actual_output_list = list()
        all_params = self.doc_parse(api_obj)
        for i in range(len(params)):
            each = params[i]
            temp = each['params']
            if each['ApiName'] == current_api:
                kwargs = self.param_type(api_obj,temp,all_params)
                actual_output_list.append(self.result_to_dict(api_obj,each['ID'],kwargs))
        return actual_output_list


    def result_to_dict(self,api_obj,id,kwargs):
        """
        送出request,把回报信息组成字典
        :param api_obj: api实例,object
        :param id: 测试用例id号,str
        :param kwargs: 入参，dict
        :return: dict()
        """
        try:
            result = api_obj(**kwargs)
            respond = {'Response Code':200,'Reason':'',
                       'Response Body':result
            }
        except ApiException,msg:
            respond = {'Response Code':msg.status,'Reason':msg.reason,
                       'Response Body':msg.body
            }
        return  {'ID':id,'respond':respond,'specified':'','params':kwargs}

    def param_type(self,api_obj,params_dict,doc_params_dict):
        """
        根据每个api方法的doc说明来转换入参格式
        :param api_obj: api实例
        :param params_dict: 需要转换格式的入参
        :param doc_params_dict: api说明中的入参
        :return:
        """
        kwargs = dict()
        temp_dict = {i:params_dict[i] for i in params_dict.keys() if i in doc_params_dict.keys() }
        for each in temp_dict:
            temp_value = temp_dict[each]
            if temp_value and doc_params_dict[each] == 'str':
                kwargs[each] = str(temp_value)
            if temp_value and doc_params_dict[each] == 'float':
                kwargs[each] = float(temp_value)
            if temp_value and doc_params_dict[each] == 'int':
                kwargs[each] = int(temp_value)
            if temp_value and doc_params_dict[each] == 'bool':
                kwargs[each] = True if int(temp_value) else False
        return kwargs