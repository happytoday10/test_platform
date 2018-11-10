from django import  forms
"""
class ProjectForm(forms.Form):
    name = forms.CharField(label='名称',max_length=100)
    describe = forms.CharField(label= "描述",widget=forms.Textarea)
    status = forms.BooleanField(label="状态")
"""
from django.forms import ModelForm
from .p_models import Project,Module

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'describe', "status")#这个的效果等同于下面一句


# class EditProjectForm(ModelForm):
#     class Meta:
#         model = Project
#         exclude= ["create_time"]
#


class ModuleForm(ModelForm):
    class Meta:
        model = Module
        #fields = ('name', 'describe', "project")#这个的效果等同于下面一句
        exclude = ["create_time"]