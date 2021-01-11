from django.shortcuts import render
from django.views.generic import View, TemplateView

import os
from hello.form import UserForm
# from hello.form import User1Form, UserModelForm


class HtmlView(TemplateView):
    template_name = "hello/test.html"   # 指定模板文件

    def post(self, request):
        print(request.POST)
        
        # 一键一值的场景
        # data = request.POST.dict()
        # print(data)

        # 一键多值的场景 getlist
        # hobby = request.POST.getlist('hobby',"")
        # print(hobby)
        # 自定义一个高效的方法
        # print(dict(request.POST))
        data1 = dict((k,','.join(v)) for k,v in dict(request.POST).items()) 
        print(data1)

        # 接收文件, 并以二进制的方式读取文件，然后存储
        # file = request.FILES.get('file',None)
        # print(file)
        # print(type(file))
        # if file:
        #     f = open(os.path.join('upload',file.name),'wb')
        #     for line in file.chunks():
        #         f.write(line)
        #     f.close()

        # 对request.POST,request.FILES进行表单验证
        form = UserForm(request.POST,request.FILES) 
        print("已经进行了表单的验证")
        if form.is_valid():
             print("表单验证OK")
             print(form.cleaned_data)
             name = form.cleaned_data['name']
             file = form.cleaned_data['file']
             print(file)
             if file:
                f = open(os.path.join('upload',file.name),'wb')
                for line in file.chunks():
                    f.write(line)
                f.close()
 
        return render(request, 'hello/test.html', {'form':form}) 

