from django.views.generic import DeleteView
from hello.models import User
from django.shortcuts import render, reverse, redirect

class IndexView(DeleteView):
    """
        删除用户
    """
    # 指定模板文件
    template_name = "hello/index.html" 
    # 获取模型中User表的数据
    model = User

    # 增加添加成功后的跳转模板       
    def get_success_url(self):
        return reverse('hello:userlist')
    
    # 查询数据--> 定义一个get请求 
    def get_context_data(self, **kwargs):
        context = super(__class__, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        print(context)
        return context