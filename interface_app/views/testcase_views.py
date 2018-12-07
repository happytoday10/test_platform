import json
import requests
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
#from interface_app.forms import TestCaseForm
from interface_app.models import TestCase
from project_app.p_models import Project,Module
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

"""
接口用例文件，返回html页面
"""


#获取用例列表
def case_manage(request):
    testcases = TestCase.objects.all()
    paginator = Paginator(testcases, 2)

    page = request.GET.get("page")
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts =paginator.page(1)#如果页数类型不是整型，取第一页
    except EmptyPage:
        #如果页数超出查询范围，取最后一页
        contacts = paginator.page(paginator.num_pages)

    if request.method == "GET":
        return render(request, "case_manage.html",{
            "type":"list",
            "testcases":contacts
        })
    else:
        return HttpResponse("404")

#搜索用例的名称
def search_case_name(request):
    if request.method == "GET":
        case_name = request.GET.get("case_name","")
        cases = TestCase.objects.filter(name__contains = case_name)

        paginator = Paginator(cases, 2)
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        return render(request,"case_manage.html",{
            "type":"list",
            "testases":contacts,
            "case_name": contacts
        })
    else:
        return HttpResponse("404")

#创建/调试用例
def add_case(request):
    if request.method =="GET":
        #form = TestCaseForm()
        print(9876)
        return render(request, "add_case.html", {
           # "form" : form,
            "type" : "add"
        })
    else:
        return HttpResponse("404")




#编辑/调试用例
def debug_case(request, cid):
    if request.method =="GET":
       # form = TestCaseForm()
        return render(request, "debug_case.html", {
           # "form" : form,
            "type" : "debug"
        })
    else:
        return HttpResponse("404")
