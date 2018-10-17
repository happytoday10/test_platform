from django.urls import  path
#from user_app import views
from project_app import  views

urlpatterns=[
    path('project_manage/',views.project_manage),
    path('add_project/', views.add_project),
    path('edit_project/',views.edit_project),

]