from django import forms
from hello.models import User
from django.views.generic import View

# 原生表单验证各种表单类型及自定义
class UserForm(forms.Form):
    # 每一个前端的字段都做个一个验证,应该和models设置的长度对应
    name = forms.CharField(max_length=20)
    password = forms.CharField(max_length=32, required=False)
    # sex = forms.CharField(max_length=10, required=False)
    phone = forms.CharField(max_length=11, required=False)
    email = forms.EmailField(required=False)
    # hobby = forms.CharField(max_length=10, required=False)
    skill = forms.CharField(max_length=10, required=False)
    file = forms.FileField()
    # info = forms.CharField(max_length=100, required=False)

    # 自定义验证格式  clean_字段
    """
    Django的form系统自动寻找匹配的函数方法，该方法名称以clean_开头，并以字段名称结束。
    如果有这样的方法，它将在校验时被调用。clean_info()方法将在指定字段的默认校验逻辑执行之后被调用。
    本例中，在必填CharField这个校验逻辑之后,）因为字段数据已经被部分处理，所以它被从self.cleaned_data
    中提取出来了。同样，我们不必担心数据是否为空，因为它已经被校验过了。
    """
    def clean_info(self):
        info = self.cleaned_data['info']
        print(info.split())
        num_info = len(info.split())
        if num_info < 4:
            raise forms.ValidationError("Info not enough words!")
        return info


class FormView(View):
    def get(self, request):
        # form = UsersForm()                      # 实例化一个表单对象，如果没有提交数据，就显示空表单
        form = UserForm()
        print(form)
        return render(request,'form.html', {'form': form}) # 空表单在前台显示    

    def post(self, request):     
        # form = UsersForm(request.POST)               # 将表单的数据绑定到form变量中
        print(form)
        form = User1Form(request.POST)
        if form.is_valid():                          # 判断用户输入的数据类型是否合法
                print(form.cleaned_data)             # 获取数据, 数据就会保存在cleaned_data的字典中
                name = form.cleaned_data['name']     # 可以获取用户提交的信息
        return render(request, 'form.html', {'form':form})  

 