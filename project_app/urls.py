from django.urls import  path
#from user_app import views
from project_app.view import project_views
from project_app.view import module_views

urlpatterns=[
    #项目
    path('project_manage/', project_views.project_manage),
    path('add_project/', project_views.add_project),
    path('edit_project/<int:pid>/', project_views.edit_project),
    path('delete_project/<int:pid>/', project_views.delete_project),

   #模块
    path('module_manage/', module_views.module_manage),
    path('add_module/', module_views.add_module),
    path('edit_module/<int:mid>/', module_views.edit_module),
    path('delete_module/<int:mid>/', module_views.delete_module),
]