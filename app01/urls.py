#! /usr/bin/env python
# encoding: utf-8
# @Time :2019/1/8 0008 下午 2:09
__Author__ = '村长'

from django.urls import path,re_path,include
from app01 import views

urlpatterns = [
    re_path(r'login/$',views.login,name="login"),
    re_path(r'index/$',views.index,name="index"),
    re_path(r'logout/$',views.logout,name="logout"),
    re_path(r'register/$',views.register,name="register"),
]