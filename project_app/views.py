from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from project_app.models import Project
# Create your views here.

  # 判断用户是否登录
@login_required
def project_manage(request):
    # return render(request,"project_manage.html")
    # 使用cookie
    # username  = request.COOKIES.get('user','')
    # return render(request,"project_manage.html",{"user":username})
    username = request.session.get('user1', '')

    # 显示出实际数据
    project_all = Project.objects.all()
    print(project_all)
    return render(request, "project_manage.html", {"user": username, "projects":project_all,
                                                   "type":"list"
                                                   })

 # 判断用户是否登录
@login_required
def add_project(request):
    #

    return render(request, "project_manage.html",{"type":"add"})

# 判断用户是否登录
@login_required
def edit_project(request):
    #

    return render(request, "project_manage.html",{"type":"edit"})