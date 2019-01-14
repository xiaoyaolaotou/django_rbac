#! /usr/bin/env python
# encoding: utf-8
# @Time :2019/1/8 0008 下午 2:09
__Author__ = '村长'

from django.urls import path,re_path,include
from rabc import views

urlpatterns = [
    re_path(r'users/$',views.users,name="users"),
    re_path(r'users/add/$',views.add_users,name="users_add"),
    re_path(r'users/delete/(\d+)/$',views.delete_users,name="users_delete"),
    re_path(r'roles/$',views.roles,name="roles"),
    re_path(r'login/$',views.login,name="login"),
    re_path(r'loginout/$',views.loginout,name="loginout"),
]




