
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="product-home"),
    path('zhantou1',views.zhantou1, name="zhantou1"),
    path('xinshidai8',views.xinshidai8, name="xinshidai8"),
    path('taishan1',views.taishan1,name="taishan1"),
    path('xiangjun1',views.xiangjun1,name="xiangjun1"),
    path('gaohua1',views.gaohua1,name="gaohua1"),
    path('upload', views.my_view, name='my-view'),
]
