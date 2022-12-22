import json
import bcrypt
import jwt
import datetime

from django.test import TestCase, Client
from django.conf import settings

from my_settings import SECRET_KEY, ALGORITHM
from .models     import User

client = Client()

class SignUpViewTest(TestCase):
    def setUp(self):
        User.objects.create(id = 1, email = 'signet@naver.com', password = 12345)

    def tearDown(self):
        User.objects.all().delete()

    def test_signup_success(self):
        data     = {'email': 'signet35@naver.com', 'password': '123456'}
        response = client.post('/user/signup', json.dumps(data), content_type='applications/json' )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "SUCCESS"})

    def test_signup_already(self):
        data     = {'email' : 'signet@naver.com', 'password' : '12345'}
        response = client.post('/user/signup', json.dumps(data), content_type='applications/json')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "USER_ALREADY_EXISTS"})

    def test_signup_noemail(self):
        data     = {'password': '12345'}
        response = client.post('/user/signup', json.dumps(data), content_type='applications/json')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "KEYERROR"})

    def test_signup_nopw(self):
        data     = {'email': 'signet@naver.com'}
        response = client.post('/user/signup', json.dumps(data), content_type='applications/json')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "KEYERROR"})

    def test_signup_invalidemail(self):
        data     = {'email': 'notemail', 'password': '12345'}
        response = client.post('/user/signup', json.dumps(data), content_type='applications/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "INVALID_EMAIL"})


class SignInViewTest(TestCase):
    def setUp(self):
        hpw  = bcrypt.hashpw('12345'.encode('utf-8'), bcrypt.gensalt())
        enpw = hpw.decode('utf-8')
        User.objects.create(id = 1, email = 'signet@naver.com', password = enpw)

    def tearDown(self):
        User.objects.all().delete()

    def test_signin_success(self):
        data     = {'email': 'signet@naver.com',  'password': '12345'}
        response = client.post('/user/signin', json.dumps(data), content_type='applications/json')
        
        user_id = User.objects.get(id=1).id
        expire  = datetime.datetime.now() + datetime.timedelta(days = 1)
        token   = jwt.encode({'user' : user_id, 'exp': expire}, SECRET_KEY, ALGORITHM)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "SUCCESS", "access_token": token})

    def test_signin_emailwrong(self):
        data     = {'email': 'signet24@naver.com', 'password': '12345'}
        response = client.post('/user/signin', json.dumps(data), content_type='applications/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "INVALID_EMAIL"})

    def test_signin_pwwrong(self):
        data     = {'email': 'signet@naver.com',  'password': '123456'}
        response = client.post('/user/signin', json.dumps(data), content_type='applications/json')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "INVALID_PASSWORD"})
        
    def test_signin_noemail(self):
        data     = {'password': '12345'}
        response = client.post('/user/signin', json.dumps(data), content_type='applications/json')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "KEYERROR"})

    def test_signup_nopw(self):
        data     = {'email': 'signet@naver.com'}
        response = client.post('/user/signin', json.dumps(data), content_type='applications/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "KEYERROR"})

