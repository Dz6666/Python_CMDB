from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, QueryDict

from hello.models import User

# 处理urls.py中定义的用户查询功能的函数
def userlist(request):
    """
        用户列表 && 姓名搜索
    """
    # 用户列表 ：查询出所有的User表中的信息
    users = User.objects.all()
     
    # 姓名搜索 ：用户查询列表就是一个GET请求，http://ip/userlist/?keyword=daizhe
    keyword = request.GET.get("keyword","")
    if keyword:     # 如果用户传来的搜索关键字则对返回数据集进行包含过滤
        users = users.filter(name__icontains=keyword)
     
    print(users)     # 打印查询输出此表的返回Queryset列表，列表中的每个元素都为一个对象
 
    # 将查询出的所有的数据传入前端，return的值，可以传递给前端模板进行渲染
    return render(request, "hello/userlist.html", {"users":users, "keyword":keyword})
