from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    return HttpResponse("HellOworld!")
    # context = { }
    # context['hello'] = 'hello world !'
    # return render(request,'hello.html',context)
def helloworld(request):
    # return HttpResponse("HELLOWORLD")
    context = { }
    context['hello'] = 'hello world !'
    return render(request,'hello.html',context)
def index(request):
    return HttpResponse("index")
def bio(request):
    return HttpResponse("biorunoob")