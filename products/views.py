from django.shortcuts import render
import json
import random

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request, *args):
    context = {
        'posts' : posts
    }
    return render(request, 'product/home.html', context)

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

    return render(request, 'product/zhantou1.html', context)

def xinshidai8(request):
    return render(request, 'product/xinshidai8.html')

def taishan1(request):
    return render(request, 'product/taishan1.html')

def xiangjun1(request):
    return render(request, 'product/xiangjun1.html')

def gaohua1(request):
    return render(request, 'product/gaohua1.html')