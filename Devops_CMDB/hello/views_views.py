from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from django.views.generic import View
from hello.models import User

class IndexView(View):
    # 用户列表
    def get(self, request):
        users = User.objects.all()
        print("view get")
        return render(request, "hello/index.html", {"users":users})
    # 用户添加
    def post(self, request):
        data = request.POST.dict()
        print(data)
        User.objects.create(**data)
        users = User.objects.all()
        return render(request, "hello/index.html", {"users":users})
    
