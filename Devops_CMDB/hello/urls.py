from django.urls import path,re_path
from . import views   

from . import views_views
from . import views_templateview
from . import views_listview
from . import views_detailview
from . import views_createview
from . import views_updateview
from . import views_deleteview

from . import cbvviews

from . import views4
app_name = 'hello'
 
# 总入口中定义/hello，这个文件为子入口中定义为/ 即放用户访问/hello 则去views模块中的index方法
urlpatterns = [

# 通用视图
    # Views
    path('views/', views_views.IndexView.as_view(), name='views'),
    # TemplateView
    path('templateview/', views_templateview.IndexView.as_view(), name='templateview'),
    # ListView --> 查询数据表的所有数据
    path('listview/', views_listview.IndexView.as_view(), name='listview'),
    # DetailView --> 查询数据表的某一条数据
    re_path('detalview/(?P<pk>[0-9]+)?/', views_detailview.IndexView.as_view(), name="detalview"),
    # CreateView --> 创建数据
    path('createview/', views_createview.IndexView.as_view(), name='createview'),
    # UpdateView --> 更新数据
	re_path('updateview/(?P<pk>[0-9]+)?/', views_updateview.IndexView.as_view(), name='updateview'),
    # DeletView --> 删除数据
    re_path('deleteview/(?P<pk>[0-9]+)?/', views_deleteview.IndexView.as_view(), name='deleteview'),

# CBV简易的用户系统版本一 ：利用编辑通用视图处理表单
    path('cbvuseradd/', cbvviews.UserAddView.as_view(), name="cbvuseradd"),
    path('cbvuserlist/', cbvviews.UserListView.as_view(), name="cbvuserlist"),
    re_path('cbvdetail/(?P<pk>[0-9]+)?/', cbvviews.UserDetailView.as_view(), name="cbvdetail"),
    re_path('cbvmodify/(?P<pk>[0-9]+)?/', cbvviews.UserUpdateView.as_view(), name="cbvmodify"),
    re_path('cbvuserdel/(?P<pk>[0-9]+)?/', cbvviews.UserDeleteView.as_view(), name="cbvuserdel"),

    # html css Jquery学习 
    path('html/', views4.HtmlView.as_view(), name="html"),

# # CBV简易的用户系统版本二 ：通过自定义表单做数据验证
#     path('useradd/', views.UserAddView.as_view(), name="user_add"),
#     path('userlist/', views.UserListView.as_view(), name="user_list"),
#     re_path('userdetail/(?P<pk>[0-9]+)?/', views.UserDetailView.as_view(), name="user_detail"),

]

