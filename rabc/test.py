#! /usr/bin/env python
# encoding: utf-8
# @Time :2019/1/11 0011 上午 11:34
__Author__ = '村长'
import re

l = ['/rabc/users/', '/rabc/users/add/', '/rabc/roles/', '/rabc/users/delete/(\d+)', '/rabc/users/edit/(\d+)']

c_path = "/rabc/users/add/"
flag = False

for permissions in l:
    permissions="^%s$" %permissions
    print(permissions)

    ret = re.match(permissions,c_path)
    if ret:
        flag = True
        break
print(flag)




