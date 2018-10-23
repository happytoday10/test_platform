from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from project_app.models import Module
from project_app.forms import ModuleForm
from django.http import HttpResponseRedirect

# Create your views here.

  # 判断用户是否登录
@login_required
def module_manage(request):
    # 模块管理
    username = request.session.get('user1', '')

    # 显示出实际数据
    module_all = Module.objects.all()
    #print(project_all)
    return render(request, "module_manage.html", {"user": username, "modules":module_all,
                                                   "type":"list"
                                                   })


@login_required
def add_module(request):
    if request.method == "POST":
        form = ModuleForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            project = form.cleaned_data['project']
            Module.objects.create(name=name,describe=describe,project=project)
            print(890)
            return HttpResponseRedirect("/manage/module_manage")
    else:
            form = ModuleForm()
    return render(request, "module_manage.html", {"form":form, "type": "add"})

@login_required
def edit_module(request, mid):
    #

    #print("到edit方法内了-mid：",mid)
    if request.method == "POST":
        form = ModuleForm(request.POST)
        if form.is_valid():
            model = Module.objects.get(id = mid)#先把原来的数据查询出来
            model.name = form.cleaned_data['name']#更新成用户重新填写的信息
            model.describe = form.cleaned_data['describe']
            model.project = form.cleaned_data['project']
            model.save()
            return HttpResponseRedirect("/manage/module_manage/")
    else:
        if mid:
            form = ModuleForm(
                instance=Module.objects.get(id = mid)
            )


    return render(request, "module_manage.html", {"form":form,
                                                  "type":"edit"
                                                   })

def delete_module(request, mid):
    #

    Module.objects.get(id=mid).delete()  # 先把原来的数据查询出来

    return HttpResponseRedirect("/manage/module_manage/")
