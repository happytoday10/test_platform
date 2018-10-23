from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from project_app.models import Project
from project_app.forms import ProjectForm
from django.http import HttpResponseRedirect

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
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']
            Project.objects.create(name=name,describe=describe,status=status)
            print(890)
            return HttpResponseRedirect("/manage/project_manage")

    else:
            form = ProjectForm()

    return render(request, "project_manage.html", {"form":form, "type": "add"})

# 判断用户是否登录
@login_required
def edit_project(request, pid):
    #

    #print("到edit方法内了-pid：",pid)
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            model = Project.objects.get(id = pid)#先把原来的数据查询出来
            model.name = form.cleaned_data['name']#更新成用户重新填写的信息
            model.describe = form.cleaned_data['describe']
            model.status = form.cleaned_data['status']
            model.save()
            return HttpResponseRedirect("/manage/project_manage/")
    else:
        if pid:
            form = ProjectForm(
                instance=Project.objects.get(id = pid)
            )


    return render(request, "project_manage.html", {"form":form,
                                                  "type":"edit"
                                                   })

@login_required
def delete_project(request, pid):
    #

    Project.objects.get(id=pid).delete()  # 先把原来的数据查询出来

    return HttpResponseRedirect("/manage/project_manage/")
