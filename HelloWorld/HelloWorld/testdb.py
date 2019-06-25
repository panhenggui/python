# -*- coding: utf8 -*-
from django.http import HttpResponse
from TestModel.models import  Test

def testdb(request):
    # test1 = Test(name='runoob')
    # test1.save()
    # return HttpResponse("<h1>数据添加成功！<h1>")
    ###################################################
    # response = ""
    # response1 = ""
    # list = Test.objects.all()
    # response2 = Test.objects.filter(id=1)
    # response3 = Test.objects.get(id=1)
    # Test.objects.order_by('name')[0:2]
    # Test.objects.order_by('id')
    # Test.objects.filter(name="runoob").order_by("id")
    # for var in list:
    #     response1 += var.name + ""
    # response = response1
    # return HttpResponse("<p>" + response + "</p>")
############################################################
    # test1 = Test.objects.get(id=1)
    # test1.name = 'Google'
    # test1.save()
    # return HttpResponse("<p>修改成功</p>")
###############################################################
    test1 = Test.objects.get(id=1)
    test1.delete()
    return HttpResponse("<h1>删除成功</h1>")

