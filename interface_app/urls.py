from django.urls import  path
from interface_app import views

urlpatterns=[

    path('case_manage/', views.case_manage),
    path('debug/', views.debug),
    path('api_debug/', views.api_debug),

]