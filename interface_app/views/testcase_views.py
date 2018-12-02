import json
import requests
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from interface_app.forms import TestCaseForm
from interface_app.models import TestCase
from project_app.p_models import Project,Module
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

#获取项目模块列表
def get_project_list(request):
    project_list = Project.objects.all()
    dataList =[]
    for project in project_list:
        project_dict = {
            "name": project.name
        }
        module_list = Module.objects.filter(project_id= project.id)
        if len(module_list) != 0:
            module_name = []
            for module in module_list:
                module_name.append(module.name)
            project_dict['moduleList'] = module_name
            dataList.append(project_dict)

    return JsonResponse({"success":"true","data": dataList})

#用例列表
def case_manage(request):
    testcases = TestCase.objects.all()
    paginator = Paginator(testcases, 2)

    page = requests.GET.get("page")
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
        form = TestCaseForm()
        return render(request, "add_case.html", {
            "form" : form,
            "type" : "add"
        })
    else:
        return HttpResponse("404")

#调试接口
def api_debug(request):
    if request.method == "POST":
        url = request.POST.get("req_url")
        method = request.POST.get("req_method")
        parameter = request.POST.get("req_method")
        payload = json.loads(parameter.repalce("","\""))
        if method =="get":
            r = requests.get(url, params=payload)



#编辑/调试用例
def debug_case(request, cid):
    if request.method =="GET":
        form = TestCaseForm()
        return render(request, "debug_case.html", {
            "form" : form,
            "type" : "debug"
        })
    else:
        return HttpResponse("404")
#获取接口信息接口
def get_case_info(request):
    if request.method == "POST":
        case_id  = request.POST.get("caseId","")
        if case_id =="":
            return JsonResponse({"success":"false","message":"case id is null"})
        case_obj = TestCase.objects.get(pk=case_id)
        #pk也是id，用它避免了关键字重复
        #打印模块的id
        print('模块id：',case_obj.module_id)
        mid = case_obj.module_id
        module_obj = Module.objects.get(id = mid)
        module_name = module_obj.name

        pid = module_obj.project_id
        print("项目id：",pid)
        project_obj = Project.objects.get(id = pid)
        project_name = project_obj.name





        case_info={
            "project_name":project_name,
            "module_name":module_name,
            "name":case_obj.name,
            "url":case_obj.url,
            "req_method":case_obj.req_method,
            "req_type":case_obj.req_type,
            "req_parameter":case_obj.req_parameter,
            "req_header":case_obj.req_header
        }
        return JsonResponse({"success": "true", "message": "ok","data":case_info})

    else:
        return HttpResponse("404")

#验证预期结果
def api_assert(request):
    if request.method == "POST":
        result_text = request.POST.get("result")
        assert_text = request.POST.get("assert","")

        if result_text =="" or assert_text == "":
            return JsonResponse({"success":"false","message":"验证的数据不能为空"})
        try:
            assert assert_text in result_text
        except AssertionError:
            return JsonResponse({"success":"false","message":"验证shibai"})
        else:
            return JsonResponse({"success":"true","message":"验证成功"})
    else:
        return JsonResponse("404")