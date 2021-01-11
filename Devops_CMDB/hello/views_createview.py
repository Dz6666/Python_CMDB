from django.views.generic import CreateView   # 导入CreateView
from hello.models import User                 # 导入model
from django.shortcuts import render, reverse, redirect
 
 
class IndexView(CreateView):
    """
        添加用户
    """
 
    # 指定模板文件
    template_name = "hello/index.html"
 
    # 获取模型中User表的数据
    model = User
 
    # 定义添加的表中的哪些列可以添加
    fields = ('name','password','sex')
 
    # 增加添加成功后的跳转模板
    success_url = 'hello:createview'
 
    # 增加添加成功后的跳转模板
    # def get_success_url(self):
    #     return reverse('hello:createview')    # 使用命名空间引用方式
 
 
   # 查询数据--> 定义一个get请求
        # 在get_context_data() 函数可以用于传递一些歪歪的内容到网页
    def get_context_data(self, **kwargs):
        # 将数据存入到context上下文中，前端渲染
            # 返回某一条数据，**kwargs为where条件，即url中传入的 pk主键
        context = super(__class__, self).get_context_data(**kwargs)
        print(kwargs)
        # 将查询到的数据库的数据全部塞到users中
        context['users'] = User.objects.all()
        print(context)
        # 将context里面数据传入到前端的index.html页面中
        return context
