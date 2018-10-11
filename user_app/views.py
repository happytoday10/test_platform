from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect

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
                #auth.login(request,user)
              #  print(3456)
              #  return render(request,"project_manage.html",{"user":user})
               # return HttpResponseRedirect("/project_manage/")
                # 使用cookie
                #response = HttpResponseRedirect('/project_manage/')

                #response.set_cookie('user',username, 3600)
                #return response
                #使用session
                request.session['user1'] = username
                return HttpResponseRedirect('/project_manage/')
            else:
                return render(request,"index.html",{"error":"用户名或密码错误！"})

def project_manage(request):
    #return render(request,"project_manage.html")
    #使用cookie
    #username  = request.COOKIES.get('user','')
    #return render(request,"project_manage.html",{"user":username})
    username = request.session.get('user1','')
    return render(request,"project_manage.html",{"user":username})

#退出登录，清除登录状态
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/')
    return response