from django.shortcuts import render,redirect,HttpResponse
from app01 import models
from functools import wraps
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from app01 import models

# Create your views here.
#
# def check_login(func):
#     """检查登录装饰器"""
#     @wraps(func)
#     def inner(request,*args,**kwargs):
#         if request.session.get("is_login") == "1":
#             return func(request,*args,**kwargs)
#         else:
#             return redirect("/app01/login/")
#     return inner
#
#
#
# def login(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#
#         user = models.User.objects.filter(username=username,password=password)
#         if user:
#             #登录成功
#             request.session["is_login"] = "1"
#             request.session["username"] = username
#             # 1. 生成特殊的字符串
#             # 2. 特殊字符串当成key，
#             # 3. 在响应中向浏览器写了一个cookie
#             return redirect("/app01/index/")
#
#     return render(request,'login.html')
#
# @check_login
# def index(request):
#     username = request.session.get("username")
#     return render(request,'index.html',{"username":username})


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("password")

        user = auth.authenticate(username=username,password=pwd)
        auth.login(request,user) #将登录的用户封装到request.user里
        if user:
            return redirect('/rabc/users/')

    return render(request,'login.html')

@login_required
def index(request):
    # username = request.user.username #获取登录用户
    return render(request,'index.html')


def logout(request):
    """注销"""
    auth.logout(request)
    return redirect("/app01/login/")


from django.contrib.auth.models import User
from app01 import models

def register(request):
    # User.objects.create_user(username="zhangsan2",password="123456")
    models.UserInfo.objects.create_user(username="lisi",password="123456")
    return HttpResponse("OK")







