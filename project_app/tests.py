from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from project_app.models import Project

# Create your tests here.
class ProjectTest(TestCase):
    # 项目管理的测试
    def setUp(self):
        # pass
        User.objects.create_user("test01","test01@email.com","123456")
        Project.objects.create(name="测试平台",describe="7877")
        self.client = Client()
        login_data = {"username":"test01","password":"123456"}
        response = self.client.post("/login_action/",login_data)

        # print(response.status_code)

    def test_project_manage(self):
        """测试项目列表."""
        response = self.client.post('/manage/project_manage/')
        project_html = response.content.decode("utf-8")
        # self.assertEqual(response.status_code, 200)
        self.assertIn("7877",project_html)

    def test_project_add(self):
        Project.objects.create(name="xiaomi8",describe="xiaomi888")
        # self.client = Client()
        response = self.client.post('/manage/project_manage/')
        project_html = response.content.decode("utf-8")
        # print(project_html)
        self.assertIn("xiaomi888",project_html)

    # 这个方法没写好。20181028
    def ktest_project_edit(self):
        # Project.objects.create(name="xiaomi8",describe="xiaomi888")
        # self.client = Client()
        project = Project.objects.filter(name="测试平台")
        project.name = "test platform"
        # project.save()
        response = self.client.post('/manage/project_manage/')
        project_html = response.content.decode("utf-8")
        print(project_html)
        self.assertIn("test platform",project_html)