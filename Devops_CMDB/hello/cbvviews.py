from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import reverse
from django.views.generic import View, TemplateView, ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from hello.models import User

class UserAddView(SuccessMessageMixin, CreateView):
    """
        创建用户
    """
    # template_name = "hello/user_form.html"  默认模板路径 hello/user_form.html（默认拼凑 {app_name}/{models_name}_form.html）
        # 源码 
            # class CreateView(SingleObjectTemplateResponseMixin, BaseCreateView):
                # """
                # View for creating a new object, with a response rendered by a template.
                # """
                # template_name_suffix = '_form'        # 子类继承后可以覆盖父类模板名称规范
    model = User     # User.objects.create(**data)
    fields = ('name','password','sex')
    success_message = "%(name)s was created successfully"


    def get_success_url(self):
        print(self.request.POST)
        if '_addanother' in self.request.POST:
            return reverse('hello:cbvuseradd')
        # return reverse("hello:cbvuserlist")

    # # CreateView继承关系
    # # CreateView -> BaseCreateView -> ModelFormMixin -> ForMixin 实现了将form最终验证结果传入前端，重写如下：
    # def from_valid(self, form):
    #     """
    #     if the form is valid, redirect to the supplied URL
    #     如果表单有效，则重定向到所提供的URL
    #     """
    #     return HttpResponseRedirect(self.get_success_url())
    
    # def form_invalid(self, form):
    #     """
    #     if the form is invalid, re-render the context data with the data-filled form and errors
    #     如果表单无效，则重新呈现上下文数据，并填充表单和错误
    #     """
    #     # 打印获取到所有前端所有的传入的信息
    #     print(form) 
    #     # 打印所有表单验证前端信息不通过的信息
    #     print(form.errors)
    #     # 打印所有表单验证前端信息不通过的信息的指定字段
    #     # print(form.name.errors)
    #     return self.render_to_response(self.get_context_data(form=form))

class UserDetailView(DetailView):
    """
    个人主页
    """
    template_name = "hello/user_detail.html"    # 默认模版路径：hello/user_detail.html 
    model = User                    # object =  User.objects.get(pk=pk) 
    context_object_name = "user"    # 自定义传给前端模板渲染的变量，默认object


class UserListView(ListView):
    """
    用户列表
    """
    # template_name = "hello/user_list.html"    # 默认模版路径：hello/user_list.html 
    model = User                    # object_list =  User.objects.all() 
    context_object_name = "users"   # 自定义传给前端模板渲染的变量，默认object_list
    keyword = ""

    # 数据过滤
    def get_queryset(self):
        queryset = super(UserListView, self).get_queryset() 
        self.keyword = self.request.GET.get("keyword","")
        if self.keyword:
            queryset = queryset.filter(name__icontains=self.keyword)
        return queryset
      
    # 需要传给前端的数据大字典
    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)  
        context['keyword'] = self.keyword
        return context 

class UserUpdateView(SuccessMessageMixin, UpdateView):
    """
    更新用户
    """
    # update和create默认的模版名都是hello/user_form.html,为了方便看，我们重写一个
    # 这两共用一个form技术上是没有问题的。生产环境中，create和update的字段可能并不完全一致，分开写更清晰
    template_name = "hello/user_edit.html"    
    model = User
    fields = ('name','password','sex')
    success_message = "%(name)s was update successfully"

    def get_success_url(self):
        if '_continue' in self.request.POST:
            return reverse('hello:cbvmodify', kwargs={'pk': self.object.pk})
        return reverse('hello:cbvuserlist')

class UserDeleteView(DeleteView):
    """
    删除用户
    """
    # template_name = 'hello/user_confirm_delete.html'  # 默认模版 hello/user_confirm_delete.html
    model = User

    def get_success_url(self):
        return reverse('hello:cbvuserlist')
