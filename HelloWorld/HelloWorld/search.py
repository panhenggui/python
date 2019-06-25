# -*- coding: utf8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response

def seach_from(request):
    return render_to_response('seach_from.html')