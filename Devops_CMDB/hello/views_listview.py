from django.views.generic import ListView   # 导入ListView
from hello.models import User           # 导入model
 
 
from django.shortcuts import render, reverse, redirect
 
class IndexView(ListView):
    """
    ListView 适合以下场景：
        getlist  :  列出所有数据
        create   :  创建数据
    """
# 公共类变量
 
    # 指定模板文件
    template_name = "hello/index.html"
 
    # 获取模板中User表的数据(objects_list = User.objects.all())
    model = User
 
    # 自定义传给前端模板渲染的变量，默认objects_list
    context_object_name = "users"
 
    keyword = ""
  
    # 定义搜索  http://ip/hello/index3/?keyword=kk
    def get_queryset(self):
        print("搜索功能")
 
        # 子类调用父类的方法拿到的所有数据User.objects.all()
        queryset = super(__class__, self).get_queryset()  
        print("data_all=",queryset)
 
        # 允许用户get请求一个keyword
        self.keyword = self.request.GET.get("keyword","")
        # 如果用户传入keywork请求，则对继承父类拿到的所有数据User.objects.all()做一个模糊查询并返回
        if self.keyword: 
            queryset = queryset.filter(name__icontains=self.keyword)
            print("keyword=",queryset)
        return queryset
  
    # 将后端的搜索关键字传入模板
    def get_context_data(self, **kwargs):
        print("搜索后的数据传入前端")
 
        # 继承基类的ListView类
        context = super(__class__, self).get_context_data(**kwargs)  # 对继承父类拿到的所有数据User.objects.all()
        print("data_all=",context)
        # 在父类的基础上，再额外加一些数据到object_list中（将查询到的数据库的数据全部塞到context中）
        context['keyword'] = self.keyword
        print("keyword=",context)
        # 将context里面数据传入到前端的index.html页面中
        return context
 
    # 提交数据--> 定义一个post请求
    def post(self, request):
        data = request.POST.dict()
        print(data)
        User.objects.create(**data)
        users = User.objects.all()
        return render(request, 'hello/index.html', {"users":users})