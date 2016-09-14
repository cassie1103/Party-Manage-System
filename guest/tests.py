#coding=utf-8
from django.test import TestCase
from guest.models import Event, Guest
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from guest.views import index  #直接引函数
from django.test import Client

# Create your tests here.
class EventTest(TestCase):

    def setUp(self):
        Event.objects.create(name="岩岩生日派对", status=True, limit=20, address="北京", start_time="2016-08-12 05:55:47.641403")

    def test_event_models(self):
        result = Event.objects.get(name="岩岩生日派对")
        self.assertEqual(result.address, "北京")
        self.assertTrue(result.status)

#测试Index首页
class IndexTest(TestCase):
    #测试根url是否解析到登录页
    def test_root_url_rewolves_to_index_page(self):
        found = resolve('/') #返回根目录127.0.0.1:8000的页面
        self.assertEqual(found.func, index)  #和index函数比较两个页面，index2.html

    #测试调用index函数返回的页与模板加载的index2.html是否相等
    def test_index_page_return_correct_html(self):
        request = HttpRequest()
        response = index(request) #HttpRequest调用的页面
        expected_html = render_to_string('index2.html')  #模板函数返回的页面
        self.assertEqual(response.content.decode(), expected_html)

#测试登录动作
class LoginActionTest(TestCase):

    def setUp(self):
        User.objects.create_user('admin', 'shijing@adwo.com', 'admin123') #创建一条用户信息

    #测试添加用户
    def test_add_author_email(self):
        user = User.objects.get(username="admin")#数据库验证
        self.assertEqual(user.email, "shijing@adwo.com")

    #用户名密码为空
    def test_login_action_username_password_null(self):
        c = Client()
        response = c.post('/login_action/',{'username':'', 'password':''})#Client中的post方法，访问login_action动作，传用户名和密码为空
        self.assertEqual(response.status_code, 200)#HTTP返回码
        self.assertIn(b"username or password null!", response.content)#返回整个页面文本，返回的是byte类型，所以文本转成byte

    def test_login_action_username_password_error(self):
        c = Client()
        response = c.post('/login_action/', {'username': '123', 'password': '123'})
        self.assertEqual(response.status_code, 200)#HTTP返回码
        self.assertIn(b"username or password error!", response.content)

    def test_login_action_username_password_success(self):
        c = Client()
        response = c.post('/login_action/', {'username': 'admin', 'password': 'admin123'})
        self.assertEqual(response.status_code, 302)

class EventManageTest(TestCase):

    def setUp(self):
        Event.objects.create(name="yanyan party", status=True, limit=20, address="beijing", start_time="2016-08-12 05:55:47.641403")

    def test_event_models(self):
        result = Event.objects.get(name="yanyan party")
        self.assertEqual(result.address, "beijing")
        self.assertTrue(result.status)

    def test_event_manage_success(self):
        c = Client()
        response = c.post('/event_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"yanyan party", response.content)
        self.assertIn(b"beijing", response.content)

class GuestManageTest(TestCase):

    def setUp(self):
        Event.objects.create(id=1, name="yanyan party", status=True, limit=20, address="beijing", start_time="2016-08-12 05:55:47.641403")
        Guest.objects.create(event_id=1, realname="helen", email="yanyan@adwo.com", phone="18911134567", sign=True)

    def test_event_models(self):
        result = Guest.objects.get(realname="helen")
        self.assertEqual(str(result.phone), "18911134567")
        self.assertEqual(result.email, "yanyan@adwo.com")
        self.assertTrue(result.sign)

    def test_guest_manage_success(self):
        c = Client()
        response = c.post('/guest_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"helen", response.content)
        self.assertIn(b"18911134567", response.content)



