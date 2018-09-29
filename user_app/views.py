from django.shortcuts import render
from django.http import  HttpResponse
from django.contrib import  auth
# Create your views here.

#wangli00 18!@#wangli
def index(request):
   # print(345)
    return render(request,"index.html")

#处理登录请求
def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username","")
        password = request.POST.get("password","")

        if username == "" or password == "":
          #  return HttpResponse("用户名或密码为空")
            return render(request,"index.html",{"error":"用户名或密码为空！"})
        else:
            user = auth.authenticate(username=username,password=password)
            print(user)
            print(type(user))
            if user is not None:
                auth.login(request,user)
                return render(request,"project_manage.html")
            else:
                return render(request,"index.html",{"error":"用户名或密码错误！"})