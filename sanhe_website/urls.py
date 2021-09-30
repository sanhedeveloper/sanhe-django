"""sanhe_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('yetou', views.yetou, name="yetou"),
    path('zhantou1',views.zhantou1, name="zhantou1"),
    path('xinshidai8',views.xinshidai8, name="xinshidai8"),
    path('taishan1',views.taishan1,name="taishan1"),
    path('xiangjun1',views.xiangjun1,name="xiangjun1"),
    path('gaohua1',views.gaohua1,name="gaohua1")
]
