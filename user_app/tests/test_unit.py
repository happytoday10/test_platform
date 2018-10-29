from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user("test01","test01@email.com","123456")
        # Animal.objects.create(name="lion", sound="roar")
        # Animal.objects.create(name="cat", sound="meow")

    def test_user(self):
        """Animals that can speak are correctly identified"""
        user = User.objects.get(username="test01")
        print(user.username)
        print(user.email)
        self.assertEqual(user.email,"test01@email.com")
        # cat = Animal.objects.get(name="cat")
        # self.assertEqual(lion.speak(), 'The lion says "roar"')
        # self.assertEqual(cat.speak(), 'The cat says "meow"')

    def test_user_create(self):
        """测试创建用户"""
        user = User.objects.create_user("test02","test02@email.com","test02")
        self.assertEqual(user.email,"test02@email.com")

    def test_user_update(self):
        """测试更新用户"""
        user = User.objects.get(username="test01")
        user.username="test02"
        user.email = "test02@email.com"
        user.save()
        self.assertEqual(user.email,"test02@email.com")

    def test_user_create(self):
        """测试delete用户"""
        user = User.objects.get(username = "test01")
        # users = User.objects.all()
        # print(len(users))
        user.delete()
        users = User.objects.all()
        # print( len(users))
        # print(users)
        self.assertEqual(len(users),0)

class IndexTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index(self):
         """测试index.html"""
         response = self.client.get('/')
         # print(response.content.decode("utf-8"))
         self.assertEqual(response.status_code, 200)
         self.assertTemplateUsed(response,"index.html")

class LoginTest(TestCase):

    def setUp(self):
        User.objects.create_user("test01","test01@email.com","123456")
        self.client = Client()

    def test_login_null(self):
         """用户名密码为空.html"""
         response = self.client.post('/login_action/')
         login_data = {"username":"","password":""}

         login_html = response.content.decode("utf-8")
         #
         self.assertEqual(response.status_code, 200)
         self.assertIn("用户名或密码为空",login_html)

    def test_login_error(self):
        """用户名密码错误.html"""
        login_data = {"username": "3", "password": "3"}
        response = self.client.post('/login_action/',login_data)


        login_html = response.content.decode("utf-8")
        #
        self.assertEqual(response.status_code, 200)
        self.assertIn("用户名或密码错误！", login_html)

    def test_login_success(self):
         """用户名密码成功.html"""

         login_data = {"username":"test01","password":"123456"}
         response = self.client.post('/login_action/',login_data)
         # login_html = response.content.decode("utf-8")

         self.assertEqual(response.status_code, 302)
         # self.assertIn("用户名或密码为空",login_html)

class LogoutTest(TestCase):
    # 这里的登出的测试，还是应该在登录成功后的测试。而不只是输入logout/
    def setUp(self):
        # pass
        User.objects.create_user("test01","test01@email.com","123456")
        self.client = Client()
        login_data = {"username":"test01","password":"123456"}
        response = self.client.post("/login_action/",login_data)
        print(response.status_code)

    def test_logout(self):
        """退出."""
        response = self.client.post('/logout/')
        project_html = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 302)