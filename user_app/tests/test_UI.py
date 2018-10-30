from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Chrome
from django.contrib.auth.models import User
from time import sleep
from project_app.models import Project

class LoginTests(StaticLiveServerTestCase):
    #fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = Chrome()
        cls.driver.implicitly_wait(10)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        User.objects.create_user("test01", "test01@email.com", "123456")
        Project.objects.create(name="项目1",describe="这个不错呦！")

    def test_login(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_id("username")
        username_input.send_keys('')
        password_input = self.driver.find_element_by_id("password")
        password_input.send_keys('')
        sleep(2)
        self.driver.find_element_by_id('submit').click()
        sleep(4)
        error_message = self.driver.find_element_by_id("error").text
        self.assertEqual("用户名或密码为空！",error_message)

    def test_login_error(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_id("username")
        username_input.send_keys('error')
        password_input = self.driver.find_element_by_id("password")
        password_input.send_keys('error')
        sleep(2)
        self.driver.find_element_by_id('submit').click()
        sleep(4)
        error_message = self.driver.find_element_by_id("error").text
        self.assertEqual("用户名或密码错误！",error_message)

    def test_login_success(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_id("username")
        username_input.send_keys('test01')
        password_input = self.driver.find_element_by_id("password")
        password_input.send_keys('123456')
        sleep(2)
        self.driver.find_element_by_id('submit').click()
        sleep(4)
        message = self.driver.find_element_by_class_name("navbar-brand").text
        self.assertEqual("测试平台", message)