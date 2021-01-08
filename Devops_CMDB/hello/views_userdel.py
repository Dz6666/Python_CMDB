from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponse, QueryDict
 
 
from hello.models import User       # 导入models，模型即数据库表
 
# 处理urls.py中定义用户删除功能的函数
from django.http import Http404
def userdel(request, **kwargs):
    """
    用户删除
    """
    msg = {}
    print(kwargs)           # 获取devops/hello/urls.py中定义的 userdel/(?P<pk>[0-9]+)?/'  所有的路由信息
    pk = kwargs.get("pk")   # pk就是devops/hello/urls.py中定义的 userdel/(?P<pk>[0-9]+)?/'  即用户ID值   {'pk': '2'}
    try:
        # 获取当前数据内容
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404
  
    #删除当前调数据
    if request.method == "POST":
        try:
            User.objects.get(pk=pk).delete()    # 根据提交的POST请求中的获取的用户ID进行删除
            msg = {"code": 0, "result": "删除用户成功"}
        except:
            msg = {"code": 1, "errmsg": "删除用户失败: %s" % traceback.format_exc()}
    # return的值，可以传递给前端模板进行渲染
    return render(request, "hello/userdel.html", {"user": user, "msg": msg})