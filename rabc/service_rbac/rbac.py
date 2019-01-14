#! /usr/bin/env python
# encoding: utf-8
# @Time :2019/1/11 0011 下午 2:11
__Author__ = '村长'
import re
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect

class ValidPermission(MiddlewareMixin):
    def process_request(self,request):
        #开放白名单，检查是否白名单
        valid_url_list = ["/rabc/login/","/rabc/reg/","/admin/.*"]

        #当前用户访问路径
        current_path = request.path_info
        # print(current_path)
        # if current_path in valid_url_list:
        #     return None #这个函数执行完毕，直接执行其它的逻辑
        #通过正则匹配,匹配白名单
        for valid_url in valid_url_list:
            ret = re.match(valid_url,current_path)
            if ret:
                return None

        #校验是否登录
        user_id = request.session.get("user_id")
        if not user_id:
            return redirect("/rabc/login/")

        #检验权限1（permission_list）
        # permission_list = request.session.get("permission_list",[])
        # # print(permission_list)
        #
        # flag = False
        # for permission in permission_list:
        #     permission = "^%s$" % permission
        #     # print(permission)
        #     ret = re.match(permission,current_path)
        #     # print("=====================")
        #     # print(ret)
        #     if ret:
        #         flag = True
        #         break
        # if not flag:
        #     return HttpResponse("你没有权限,滚!!!")

        # 校验权限2（permission_dict）
        permission_dict = request.session.get("permission_dict")

        for item in permission_dict.values():
            # print(item)
            urls = item['urls']
            for reg in urls:
                reg = "^%s$"%reg
                ret = re.match(reg,current_path)
                if ret:
                    # print(item['urls'])
                    # print(item['actions'])
                    request.actions = item['actions']
                    return None
        return HttpResponse("你没有权限，快滚！！！")







