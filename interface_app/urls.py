from django.urls import  path
from interface_app.views import testcase_views
from interface_app.views import testcase_api

urlpatterns=[

    #用例管理
    path('case_manage/', testcase_views.case_manage),
    path('add_case/', testcase_views.add_case),
    path('search_case_name/', testcase_views.search_case_name),
    path('debug_case/<int:cid>/', testcase_views.debug_case),
    #path('get_case_info/', testcase_views.get_case_info),




    path('api_debug/', testcase_api.api_debug),


    path('save_case/', testcase_api.save_case),



]