from django.shortcuts import render
import json
import random

def index(request):
    return render(request, 'index.html')

def yetou(request):
    return render(request, 'yetou.html')

def zhantou1(request, *args, **kwargs):
    context = {}
    context['hist1'] = [10,30,20,40]
    context['hist15'] = [10,30,20,40,60,50]
    context['hist51'] = [10,30,20,40,60,70,80,90]
    context['hist530'] = [10,30,20,40,60,70,80,90,110,120,140,110,150]
    context['histMonth11'] = [10,30,20,40,60,70,80,90,110,120,140,110,150,200,160]
    context['histYear'] = [10,30,20,40,60,70,80,90,110,120,140,110,150,200,160,180,200,170,120,220]

    return render(request, 'zhantou1.html', context)

def xinshidai8(request):
    return render(request, 'xinshidai8.html')

def taishan1(request):
    return render(request, 'taishan1.html')

def xiangjun1(request):
    return render(request, 'xiangjun1.html')

def gaohua1(request):
    return render(request, 'gaohua1.html')