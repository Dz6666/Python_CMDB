from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, QueryDict
from hello.models import User       # 导入module,模型即数据库表
 
 
import traceback                    # traceback模块被用来跟踪异常返回值
 
# 处理urls.py中定义用户添加功能的函数
def useradd(request):
    """
        添加用户 ：用户添加分为 get请求和post请求
            request 获取表单提交的数据有多种方式：
                1、request.POST.get()  --> 适用于获取单个变量进行处理的场景
                2、request.POST.dict() --> 适用于将表单所有的数据整体处理的场景
                3、From(request.POST)  --> 适用于表单类验证的场景（生产中最常用）
    """
 
    # 自定义用户页面返回信息（成功/失败）
    msg = {}
    # 用户打开页面默认是一个GET请求，创建用户默认是一个POST提交请求
    print("get")
 
    # 通过判断用户请求的 method 方法判断用户是 GET请求还是POST请求
    if request.method == "POST":
        try:
            print(request.POST)     # 获取相应信息中post发送的数据
             
            # 方法一 ：一个个获取值，然后一个个入库，但是代码不优雅
            # name = request.POST.get('name',"")
            # password = request.POST.get('password',"")
            # sex = request.POST.get('sex',"")
            # print(name, password, sex)
            # u = User
            # u.name = name
            # u.password = password
            # u.sex = sex
            # u.save()
 
            # 方法二 ：将提交的数据转为字典，一次性入库
            data = request.POST.dict()
            print(data)
            User.objects.create(**data)     # 接收POST请求的数据存入到字典中，解构方式写入数据库
            msg = {"code":0, "result":"用户添加成功"}
        except:
        # except Exception as e:
            # msg =  {"code": 1, "errmsg": "用户添加失败: %s" %e}
            msg =  {"code": 1, "errmsg": "用户添加失败: %s" % traceback.format_exc()}
 
    return render(request,"hello/useradd.html", {"msg":msg})    # 将msg传入前端