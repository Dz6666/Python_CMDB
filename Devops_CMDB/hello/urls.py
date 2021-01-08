from django.urls import path,re_path
from . import views   

from . import views_views
from . import views_templateview
from . import views_listview
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
]
