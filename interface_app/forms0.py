from django.forms import ModelForm
from interface_app.models import TestCase


"""
interface_app没有用到form文件，因为数据大都是直接通过接口获取的，没有用到django的form
跟之前的project_app是不同的思路
"""
class TestCaseForm(ModelForm):
    class Meta:
        model = TestCase
        fields = ('module')#这里用小括号写对吗？
        # exclude = ["create_time"]