"""test_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from user_app import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index),
    path("login_action/",views.login_action),
    path("logout/",views.logout),
    path("accounts/login/",views.index),
   # path('project_manage/',views.project_manage),
    #path("add_project/", views.add_project)

    #这里把一级目录是manage的指定到 project_app目录下的urls文件
     path("manage/",include("project_app.urls"))
]

#初始化数据库：python manage.py migrate
#创建超级管理员 python manage.py createsuperuser   admin 123456