from django.views.generic import DetailView   # 导入DetailView
from hello.models import User                 # 导入model
from datetime import datetime, timezone
# from django.shortcuts import render, reverse, redirect
# from django.http import HttpResponse, QueryDict

print(User.objects.all())
 
class IndexView(DetailView):
    """
        获取某条记录ID，适用于下面三种场景：核心就是拿到URL中的ID
            getone : 获取当前记录数据
            update : 更新当前记录数据
            delete ：删除当前记录数据
    """
 
    # 指定前端渲染模板，不指定默认为delail.html
    template_name = "hello/index.html"
 
    # 获取模型中User表的数据（object_detail = User.objects.get(pk=pk)）
    model = User
     
 
    # 自定义传给前端模板渲染的变量，默认object
    # context_object_name = "users"
 
    # 查询数据--> 定义一个get请求
        # 在get_context_data() 函数可以用于传递一些额外的内容到网页
    def get_context_data(self, **kwargs):
        # 将数据存入到context上下文中，前端渲染
            # 返回某一条数据，**kwargs为where条件，即url中传入的 pk主键
        context = super(__class__, self).get_context_data(**kwargs)
        print(kwargs)
        # 将查询到的数据库的数据全部塞到users中
        context['users'] = User.objects.all()
        print(context)
            # {'view': <hello.views2.IndexView4 object at 0x00000276775CC5C0>, 'users': <QuerySet [<User: daizhe>, <User: mana>, <User: mana1>, <User: mana2>, <User: mana3>, <User: mana5>, <User: daizhe2>, <User: mana6>, <User: daizhe3>]>}
        # 将context里面数据传入到前端的index.html页面中
        return context