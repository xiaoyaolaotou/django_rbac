from django.shortcuts import render,HttpResponse,redirect
from rabc import models
from rabc.service_rbac import permission



def login(request):
    if request.method == "POST":
        user = request.POST.get("username")
        pwd = request.POST.get("password")

        user = models.User.objects.filter(name=user,pwd=pwd).first()
        # print(user)
        if user:
            #在session中注册登录用户ID
            request.session["user_id"] = user.pk
            #把封装好的权限导入
            permission.initial_session(user,request)

            return redirect("/rabc/users/")
            # return HttpResponse("OK")
    return render(request,'login.html')


def loginout(request):
    # request.session.remove()
    return redirect('/rabc/login/')



def users(request):
    user_id = request.session.get("user_id")
    obj = models.User.objects.filter(id=user_id).first()

    user_list = models.User.objects.all()
    # permission_list = request.session.get('permission_dict')

    #获取当前用户应该放到菜单栏的权限
    menu_permission_list = request.session['menu_permission_list']


    return render(request,"users.html",{'user_list':user_list,'username':obj,'menu_permission_list':menu_permission_list})

import re
def add_users(request):
    # permission_list = request.session["permission_list"]
    # current_path = request.path_info
    #
    # flag = False
    # for permission in permission_list:
    #     permission = "^%s$" %permission
    #     ret = re.match(permission,current_path)
    #     if ret:
    #         flag = True
    #         break
    #     return HttpResponse("你没有权限,滚")
    return HttpResponse("add users")


def delete_users(request,id):

    return HttpResponse("del"+id)


def roles(request):

    roles_list = models.Role.objects.all()
    per_permission_list = request.session['menu_permission_list']
    return render(request,'roles.html',{'roles_list':roles_list,'per_permission_list':per_permission_list})






