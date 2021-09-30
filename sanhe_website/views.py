from django.shortcuts import render
import json
import random

def index(request):
    return render(request, 'index.html')

def yetou(request):
    return render(request, 'yetou.html')
