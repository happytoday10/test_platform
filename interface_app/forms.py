from django.forms import ModelForm
from interface_app.models import TestCase

class TestCaseForm(ModelForm):
    class Meta:
        model = TestCase
        fields = ('module')#这里用小括号写对吗？
        # exclude = ["create_time"]