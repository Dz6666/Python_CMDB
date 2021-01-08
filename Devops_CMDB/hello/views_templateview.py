from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from django.views.generic import TemplateView
from hello.models import User

class IndexView(TemplateView):
    # 指定模板文件
    template_name = "hello/index.html"

    # 数据查询
    def get_context_data(self, **kwargs):
        # 将数据存入到context上下文中，供前端渲染
        context = super(IndexView, self).get_context_data(**kwargs)
        print('----', kwargs)
    
        # 将数据库查询的数据全部塞到users中，并将users传入到前端模板进行渲染
        context['users'] = User.objects.all()
        print('....', context)
    
    # 数据提交
    def post(self, request):
        data = request.POST.dict()
        print(data)
        User.objects.create(**data)
        users = User.objects.all()
        return render(request, "hello/index.html", {"users":users})


