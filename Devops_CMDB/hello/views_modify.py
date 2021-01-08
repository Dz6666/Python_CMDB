from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponse, QueryDict
import traceback
 
from hello.models import User       # 导入models，模型即数据库表
 
# 处理urls.py中定义用户更新功能的函数
from django.shortcuts import get_object_or_404
from django.http import Http404
    # get_objects_or_404 是用来返回HTTP请求
    # 格式: get_objects_or_404(models, **kwargs)
  
def modify(request, **kwargs):  # **kwargs参数收集
    """
        用户更新:
            1.通过ID拿到要更新的数据,并传到前端渲染
            2.将修改后的数据提交到后端
    """
    msg = {}
    print(kwargs)            # 获取devops/hello/urls.py中定义的 modify/(?P<pk>[0-9]+)?/'  所有的路由信息 {'pk': '2'}
    pk = kwargs.get("pk")    # pk就是devops/hello/urls.py中定义的 modify/(?P<pk>[0-9]+)?/'  即用户ID值  2
  
    # user = User.objects.get(pk=pk)         # 不严谨,用户ID不存在则报错
    user = get_object_or_404(User, pk=pk)    # 先查询用户传入的ID是否存在,如果存在则往下走,如果不存在则抛异常404
  
    # 提交更新过的数据到数据库
    if request.method == "POST":
        try:
            data = request.POST.dict()  # 获取到POST,并转换成字典
                                        # <QuerySet [<User: daizhe>, <User: mana>, <User: mana1>, <User: mana2>, <User: mana3>, <User: dasdasdawd>, <User: mana5>, <User: daizhe2>, <User: mana6>]>
            print(data)
            User.objects.filter(pk=pk).update(**data)  # 过滤出更新的字段并更新数据库
            msg = {"code": 0, "result": "更新用户成功"}
        # except Exception sa e:
        except:
            msg = {"code": 1, "errmsg": "更新用户失败: %s" % traceback.format_exc()}
            # msg = {"code": 1, "errmsg": "更新用户失败: %s" % e }
    # return的值，可以传递给前端模板进行渲染
    return render(request, "hello/modify.html", {"user":user, "msg":msg})
        