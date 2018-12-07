from django.contrib import admin
from interface_app.models import TestCase,TestTask

# Register your models here.


class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['module','name','url','req_method',"req_type",
                    "req_header","req_parameter","response_assert"]

class TestTackAdmin(admin.ModelAdmin):
    list_display = ['name','describe','class']

admin.site.register(TestCase,TestCaseAdmin)
admin.site.register(TestTask,TestTackAdmin)