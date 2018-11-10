from django.forms import ModelForm
from project_app.p_models import Module

class TestCaseForm(ModelForm):
    class Meta:
        model = Module
        fields = ('name')#这里用小括号写对吗？
        # exclude = ["create_time"]