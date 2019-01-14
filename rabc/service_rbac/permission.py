#! /usr/bin/env python
# encoding: utf-8
# @Time :2019/1/11 0011 下午 2:48
__Author__ = '村长'

def initial_session(user,request):
    #方案一：
    # # 查询当前登录用户的所有权限
    # permissions = user.roles.all().values("permissions__url").distinct()
    # permission_list = []
    # #对values格式进行处理
    # for item in permissions:
    #     #把URL存入在一个列里，存URL路径
    #     permission_list.append(item["permissions__url"])
    # print(permission_list)
    #
    # # 在session中注同登录用户的权限列表
    # request.session["permission_list"] = permission_list


    #方案二：
    permissions = user.roles.all().values("permissions__url","permissions__group_id","permissions__action").distinct()
    # print(permissions)
    permission_dict = {}

    for item in permissions:
        gid = item.get('permissions__group_id')
        if not gid in permission_dict:
            permission_dict[gid] = {
                'urls':[item['permissions__url'],],
                'actions':[item['permissions__action'],],
            }
        else:
            permission_dict[gid]['urls'].append(item['permissions__url'])
            permission_dict[gid]['actions'].append(item['permissions__action'])
    #注册session
    request.session["permission_dict"] = permission_dict
    # print(permission_dict)


    #注册左侧菜单权限是否显示
    permissions = user.roles.all().values("permissions__url","permissions__action","permissions__group__title").distinct()
    print("al:",permissions)
    menu_permission_list = []
    for item in permissions:
        if item['permissions__action'] == 'list':
            menu_permission_list.append((item['permissions__url'],item['permissions__group__title']))
    print(menu_permission_list)
    request.session['menu_permission_list'] = menu_permission_list




