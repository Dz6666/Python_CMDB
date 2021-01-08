"""Devops_CMDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls import path,include
# 如果hello，总入口直接指向具体app的具体方法，一旦app过多，路由过多，主入口则不堪重负，要分而治之。
# 在主站的urls.py文件中指定，当用户访问hello的时候，我不指定具体的方法，而是告诉用户去hello的app的urls.py子路由文件查找。
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')),
]