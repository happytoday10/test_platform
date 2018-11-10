from django.db import models

# Create your models here.
#python manage.py makemigrations生成对应的
#在执行python manage.py migrate

#class = table  user_app_project
#变量 = 字段（类型，长度）
class Project(models.Model):
    """
    项目表
    auto_now=True，这里指不指定，就默认为当前时间
    """
    name = models.CharField("名称",max_length=100,blank=False,default="")
    describe = models.TextField("描述",default="")
    status = models.BooleanField("状态",default="True")
    create_time = models.DateTimeField("创建时间",auto_now=True)

#这个方法是让项目显示项目的名称
    def __str__(self):
        return self.name

class Module(models.Model):
    """
    模块表
    注意下面的CASCADE后面没有小括号()
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField("名称",max_length=100, blank=False, default="")
    describe = models.TextField("描述",default="")
    create_time = models.DateTimeField("创建时间",auto_now=True)

    def __str__(self):
        return self.name