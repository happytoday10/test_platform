from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
import json
from interface_app.forms import TestCaseForm
# Create your views here.

def case_manage(request):
    if request.method == "GET":
        return render(request,"case_manage.html",
                      { "type":"list"})
    else:
        return HttpResponse("404")

#创建调试接口
def debug(request):
    if request.method == "GET":
        form = TestCaseForm()
        return render(request,"api_debug.html",{
            "form": form,
            "type" : "debug"
        })
    else:
        return HttpResponse("404")

#调试接口
def api_debug(request):
    if request.method == "POST":
        url = request.POST.get("req_url")
        method = request.POST.get("req_method")
        parameter = request.POST.get("req_parameter")
        print(parameter)
        print(type(parameter))
        parameter_dict = json.load(parameter.replace("\"","'"))

        print(type(parameter))
        if method == "get":
            r = requests.get(url,params=parameter_dict)
        if method == "post":
                # 这里拿到url，使用get还时post----shi post
            r = requests.post(url,data=parameter_dict)
        print(r)
        print(r.text)
            # resp = r.json()
        return HttpResponse(r.text)
    else:
        return render(request, "api_debug.html", {
                "type": "debug"
            })

def save_case(request):
    """
    保存用例
    """
    if request.method == "POST":
        url = request.POST.get("req_url")
        method = request.POST.get("req_method")
        parameter = request.POST.get("req_parameter")
        req_type = request.POST.get("req_type")
        header = request.POST.get("header")
        module_id = request.POST.get("module_id")

    else:
        return render(request, "api_debug.html", {
                "type": "debug"
            })