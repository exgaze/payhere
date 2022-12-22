import json
import bcrypt
import jwt
import datetime
import pyshorteners
import socket
import freezegun

from django.test import TestCase, Client

from my_settings    import SECRET_KEY, ALGORITHM
from .models        import ShortURL
from account.models import Memo, AccountHistory
from user.models    import User

client = Client()

def tokenmaker(data, exp):
    key = SECRET_KEY
    alg = ALGORITHM

    if exp:
        expire = datetime.datetime.now() + datetime.timedelta(days=1)
        token  = jwt.encode({'user': data, 'exp': expire}, key, alg)
        return token
    
    expire = datetime.datetime.now() - datetime.timedelta(days=1)
    token  = jwt.encode({'user': data, 'exp': expire}, key, alg)
    return token

class URLShortnerView(TestCase):
    def setUp(self):
        hpw   = bcrypt.hashpw('12345'.encode('utf-8'), bcrypt.gensalt())
        enpw  = hpw.decode('utf-8')
        
        user1 = User.objects.create(id       = 1, 
                                    email    = 'signet@naver.com', 
                                    password = enpw)

        acc1 = AccountHistory.objects.create(id            = 1,
                                            user           = user1,
                                            date           = datetime.date.today(),
                                            detail_expense = 10000)


        acc2 = AccountHistory.objects.create(id            = 2,
                                            user           = user1,
                                            date           = datetime.date.today() + datetime.timedelta(days=1),
                                            detail_expense = 10000)

        acc3 = AccountHistory.objects.create(id            = 3,
                                            user           = user1,
                                            date           = datetime.date.today() + datetime.timedelta(days=2),
                                            detail_expense = 10000)

        Memo.objects.create(id      = 1, 
                            expense = acc1,
                            content = '1')
        
        Memo.objects.create(id      = 2, 
                            expense = acc2,
                            content = '2')

        Memo.objects.create(id      = 3,
                            expense = acc3,
                            content = '3')

        host  = socket.gethostbyname(socket.gethostname())
        url   = {'url' : host + '/account/list'}
        surl  = pyshorteners.Shortener().chilpit.short(url)[7:]
        url2  = {'url' : host + '/account/history'}
        surl2 = pyshorteners.Shortener().chilpit.short(url)[7:]
        
        ShortURL.objects.create(id=1, urlorigin = url, urlshorten = surl)
        ShortURL.objects.create(id=2, urlorigin = url2, urlshorten = surl2)
    
    def tearDown(self):
        User.objects.all().delete()
        AccountHistory.objects.all().delete()
        Memo.objects.all().delete()
        ShortURL.objects.all().delete()

    def test_URLshortner_post_success(self):
        user_id = User.objects.get(id=1).id
        headers = {'HTTP_AUTHORIZATION': tokenmaker(user_id, True)}
        host    = socket.gethostbyname(socket.gethostname())
        url     = {'url' : host + '/account/history/1'}
        
        response = client.post('/short', json.dumps(url), content_type='application/json', **headers)
        
        surl = list(ShortURL.objects.all())[-1].urlshorten
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["data"], 'http://chilp.it/' + surl)

    def test_URLshortner_post_keyerror(self):
        user_id = User.objects.get(id=1).id
        headers = {'HTTP_AUTHORIZATION': tokenmaker(user_id, True)}
        url = {}

        response = client.post('/short', json.dumps(url), content_type='application/json', **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "KEYERROR"})

class RedirectView(TestCase):
    def setUp(self):
        hpw   = bcrypt.hashpw('12345'.encode('utf-8'), bcrypt.gensalt())
        enpw  = hpw.decode('utf-8')
        
        user1 = User.objects.create(id       = 1, 
                                    email    = 'signet@naver.com', 
                                    password = enpw)

        acc1 = AccountHistory.objects.create(id            = 1,
                                            user           = user1,
                                            date           = datetime.date.today(),
                                            detail_expense = 10000)


        acc2 = AccountHistory.objects.create(id            = 2,
                                            user           = user1,
                                            date           = datetime.date.today() + datetime.timedelta(days=1),
                                            detail_expense = 10000)

        acc3 = AccountHistory.objects.create(id            = 3,
                                            user           = user1,
                                            date           = datetime.date.today() + datetime.timedelta(days=2),
                                            detail_expense = 10000)

        Memo.objects.create(id      = 1, 
                            expense = acc1,
                            content = '1')
        
        Memo.objects.create(id      = 2, 
                            expense = acc2,
                            content = '2')

        Memo.objects.create(id      = 3,
                            expense = acc3,
                            content = '3')

        host  = socket.gethostbyname(socket.gethostname())
        url   = 'http://' + host + '/account/list'
        surl  = pyshorteners.Shortener().chilpit.short(url)[16:]
        url2  = 'http://' + host + '/account/history'
        surl2 = pyshorteners.Shortener().chilpit.short(url2)[16:]
        
        ShortURL.objects.create(id=1, urlorigin = url, urlshorten = surl)
        ShortURL.objects.create(id=2, urlorigin = url2, urlshorten = surl2)

    def tearDown(self):
        User.objects.all().delete()
        AccountHistory.objects.all().delete()
        Memo.objects.all().delete()
        ShortURL.objects.all().delete()

    def test_redirectview_success(self):
        user_id = User.objects.get(id=1).id
        headers = {'HTTP_AUTHORIZATION': tokenmaker(user_id, True)}
        surl    = ShortURL.objects.get(id=1).urlshorten

        response = client.get('/chilp.it/' + surl, content_type='application/json', **headers)
        self.assertEqual(response.status_code, 302)
    
    @freezegun.freeze_time("2100-01-01")
    def test_redirectview_expired(self):
        user_id = User.objects.get(id=1).id
        headers = {'HTTP_AUTHORIZATION': tokenmaker(user_id, True)}
        surl    = ShortURL.objects.get(id=1).urlshorten
        
        response = client.get('/chilp.it/' + surl, content_type='application/json', **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message" : "URLEXPIRED"})


