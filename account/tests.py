import json
import bcrypt
import jwt
import datetime

from django.test import TestCase, Client

from my_settings import SECRET_KEY, ALGORITHM
from .models     import Memo, AccountHistory
from user.models import User

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

class AccountListViewTest(TestCase):
    def setUp(self):
        hpw  = bcrypt.hashpw('12345'.encode('utf-8'), bcrypt.gensalt())
        enpw = hpw.decode('utf-8')
        
        user1 = User.objects.create(id       = 1, 
                                    email    = 'signet@naver.com', 
                                    password = enpw)

        user2 = User.objects.create(id       = 2, 
                                    email    = 'signet2@naver.com', 
                                    password = enpw)

        user3 = User.objects.create(id       = 3, 
                                    email    = 'signet3@naver.com', 
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

        acc4 = AccountHistory.objects.create(id            = 4,
                                            user           = user2,
                                            date           = datetime.date.today(),
                                            detail_expense = 10000)

        acc5 = AccountHistory.objects.create(id            = 5,
                                            user           = user2,
                                            date           = datetime.date.today(),
                                            detail_expense = 10000)

        acc6 = AccountHistory.objects.create(id            = 6,
                                            user           = user2,
                                            date           = datetime.date.today(),
                                            detail_expense = 10000)

        acc7 = AccountHistory.objects.create(id            = 7,
                                            user           = user3,
                                            date           = datetime.date.today() + datetime.timedelta(days=1),
                                            detail_expense = 10000)

        acc8 = AccountHistory.objects.create(id            = 8,
                                            user           = user3,
                                            date           = datetime.date.today() + datetime.timedelta(days=1),
                                            detail_expense = 10000)

        acc9 = AccountHistory.objects.create(id            = 9,
                                            user           = user3,
                                            date           = datetime.date.today() + datetime.timedelta(days=3),
                                            detail_expense = 10000)

        acc10 = AccountHistory.objects.create(id           = 10,
                                            user           = user3,
                                            date           = datetime.date.today() + datetime.timedelta(days=3),
                                            detail_expense = 10000)

        acc11 = AccountHistory.objects.create(id           = 11,
                                            user           = user3,
                                            date           = datetime.date.today() + datetime.timedelta(days=3),
                                            detail_expense = 10000)

        acc12 = AccountHistory.objects.create(id           = 12,
                                            user           = user3,
                                            date           = datetime.date.today() + datetime.timedelta(days=5),
                                            detail_expense = 10000)

        acc13 = AccountHistory.objects.create(id           = 13,
                                            user           = user3,
                                            date           = datetime.date.today() + datetime.timedelta(days=5),
                                            detail_expense = 10000)

        acc14 = AccountHistory.objects.create(id           = 14,
                                            user           = user3,
                                            date           = datetime.date.today() + datetime.timedelta(days=5),
                                            detail_expense = 10000)

        acc15 = AccountHistory.objects.create(id           = 15,
                                            user           = user3,
                                            date           = datetime.date.today() + datetime.timedelta(days=5),
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

        Memo.objects.create(id      = 4, 
                            expense = acc4,
                            content = '4')

        Memo.objects.create(id      = 5, 
                            expense = acc5,
                            content = '5')

        Memo.objects.create(id      = 6, 
                            expense = acc6,
                            content = '6')

        Memo.objects.create(id      = 7, 
                            expense = acc7,
                            content = '7')

        Memo.objects.create(id      = 8, 
                            expense = acc8,
                            content = '8')

        Memo.objects.create(id      = 9, 
                            expense = acc9,
                            content = '9')

        Memo.objects.create(id      = 10, 
                            expense = acc10,
                            content = '10')

        Memo.objects.create(id      = 11, 
                            expense = acc11,
                            content = '11')

        Memo.objects.create(id      = 12, 
                            expense = acc12,
                            content = '12')

        Memo.objects.create(id      = 13, 
                            expense = acc13,
                            content = '13')

        Memo.objects.create(id      = 14, 
                            expense = acc14,
                            content = '14')

        Memo.objects.create(id      = 15, 
                            expense = acc15,
                            content = '15')

    def tearDown(self):
        User.objects.all().delete()
        AccountHistory.objects.all().delete()
        Memo.objects.all().delete()

    def test_list_success(self):
        user_id = User.objects.get(id=1).id
        headers = {'HTTP_AUTHORIZATION': tokenmaker(user_id, True)}

        response = client.get('/account/list', content_type='application/json', **headers)
        
        date = datetime.date.today()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data'], [{str(date) : 10000}, 
                                                    {str(date + datetime.timedelta(days=1)) : 10000},
                                                    {str(date + datetime.timedelta(days=2)) : 10000}])

        user_id = User.objects.get(id=2).id
        headers = {'HTTP_AUTHORIZATION': tokenmaker(user_id, True)}

        response = client.get('/account/list', content_type='application/json', **headers)
        date     = datetime.date.today()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data'], [{str(date) : 30000}])

        user_id = User.objects.get(id=3).id
        headers = {'HTTP_AUTHORIZATION': tokenmaker(user_id, True)}

        response = client.get('/account/list', content_type='application/json', **headers)
        
        date = datetime.date.today()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data'], [{str(date + datetime.timedelta(days=1)) : 20000}, 
                                                    {str(date + datetime.timedelta(days=3)) : 30000},
                                                    {str(date + datetime.timedelta(days=5)) : 40000}])

    def test_not_login(self):
        response = client.get('/account/list', content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "NEED_LOGIN"})

    def test_expired_token(self):
        user_id = User.objects.get(id=1).id
        headers = {'HTTP_AUTHORIZATION': tokenmaker(user_id, False)}

        response = client.get('/account/list', content_type='application/json', **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "INVALID_TOKEN"})

    def test_invalid_user(self):
        headers = {'HTTP_AUTHORIZATION': tokenmaker(4, True)}

        response = client.get('/account/list', content_type='application/json', **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "INVALID_USER"})


class AccountHistoryViewTest(TestCase):
    def setUp(self):
        hpw  = bcrypt.hashpw('12345'.encode('utf-8'), bcrypt.gensalt())
        enpw = hpw.decode('utf-8')
        
        user1 = User.objects.create(id       = 1, 
                                    email    = 'signet@naver.com', 
                                    password = enpw)

        user2 = User.objects.create(id       = 2, 
                                    email    = 'signet2@naver.com', 
                                    password = enpw)

        user3 = User.objects.create(id       = 3, 
                                    email    = 'signet3@naver.com', 
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

        acc4 = AccountHistory.objects.create(id            = 4,
                                            user           = user2,
                                            date           = datetime.date.today(),
                                            detail_expense = 10000)

        acc5 = AccountHistory.objects.create(id            = 5,
                                            user           = user2,
                                            date           = datetime.date.today(),
                                            detail_expense = 10000)

        acc6 = AccountHistory.objects.create(id            = 6,
                                            user           = user2,
                                            date           = datetime.date.today(),
                                            detail_expense = 10000)

        acc7 = AccountHistory.objects.create(id            = 7,
                                            user           = user3,
                                            date           = datetime.date.today() + datetime.timedelta(days=1),
                                            detail_expense = 10000)

        acc8 = AccountHistory.objects.create(id            = 8,
                                            user           = user3,
                                            date           = datetime.date.today() + datetime.timedelta(days=1),
                                            detail_expense = 10000)

        acc9 = AccountHistory.objects.create(id            = 9,
                                            user           = user3,
                                            date           = datetime.date.today() + datetime.timedelta(days=3),
                                            detail_expense = 10000)

        acc10 = AccountHistory.objects.create(id           = 10,
                                            user           = user3,
                                            date           = datetime.date.today() + datetime.timedelta(days=3),
                                            detail_expense = 10000)

        acc11 = AccountHistory.objects.create(id           = 11,
                                            user           = user3,
                                            date           = datetime.date.today() + datetime.timedelta(days=3),
                                            detail_expense = 10000)

        acc12 = AccountHistory.objects.create(id           = 12,
                                            user           = user3,
                                            date           = datetime.date.today() + datetime.timedelta(days=5),
                                            detail_expense = 10000)

        acc13 = AccountHistory.objects.create(id           = 13,
                                            user           = user3,
                                            date           = datetime.date.today() + datetime.timedelta(days=5),
                                            detail_expense = 10000)

        acc14 = AccountHistory.objects.create(id           = 14,
                                            user           = user3,
                                            date           = datetime.date.today() + datetime.timedelta(days=5),
                                            detail_expense = 10000)

        acc15 = AccountHistory.objects.create(id           = 15,
                                            user           = user3,
                                            date           = datetime.date.today() + datetime.timedelta(days=5),
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

        Memo.objects.create(id      = 4, 
                            expense = acc4,
                            content = '4')

        Memo.objects.create(id      = 5, 
                            expense = acc5,
                            content = '5')

        Memo.objects.create(id      = 6, 
                            expense = acc6,
                            content = '6')

        Memo.objects.create(id      = 7, 
                            expense = acc7,
                            content = '7')

        Memo.objects.create(id      = 8, 
                            expense = acc8,
                            content = '8')

        Memo.objects.create(id      = 9, 
                            expense = acc9,
                            content = '9')

        Memo.objects.create(id      = 10, 
                            expense = acc10,
                            content = '10')

        Memo.objects.create(id      = 11, 
                            expense = acc11,
                            content = '11')

        Memo.objects.create(id      = 12, 
                            expense = acc12,
                            content = '12')

        Memo.objects.create(id      = 13, 
                            expense = acc13,
                            content = '13')

        Memo.objects.create(id      = 14, 
                            expense = acc14,
                            content = '14')

        Memo.objects.create(id      = 15, 
                            expense = acc15,
                            content = '15')

    def tearDown(self):
        User.objects.all().delete()
        AccountHistory.objects.all().delete()
        Memo.objects.all().delete()

    def test_history_post_success(self):
        user    = User.objects.get(id=2)
        headers = {'HTTP_AUTHORIZATION': tokenmaker(user.id, True)}
        data    = {'date': str(datetime.date.today()), 'expense': 10000, 'memo': 'test'}

        response = client.post('/account/history', json.dumps(data), content_type='application/json', **headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "SUCCESS"})

        newexpense = list(AccountHistory.objects.filter(user=user))[-1]
        newmemo    = Memo.objects.get(expense = newexpense)
        
        self.assertTrue(data['date'] == str(newexpense.date)
                        and data['expense'] == newexpense.detail_expense
                        and data['memo'] == newmemo.content)

    def test_history_post_keyerror(self):
        user    = User.objects.get(id=1)
        headers = {'HTTP_AUTHORIZATION': tokenmaker(user.id, True)}
        data    = {'date': str(datetime.date.today()), 'expense': 10000}

        response = client.post('/account/history', json.dumps(data), content_type='application/json', **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "KEYERROR"})

    def test_history_get_success(self):
        user    = User.objects.get(id=2)
        headers = {'HTTP_AUTHORIZATION': tokenmaker(user.id, True)}
        date    = str(datetime.date.today()).replace('-', '')
        
        response = client.get('/account/history/'+ date, content_type='application/json', **headers)
        
        expenses = AccountHistory.objects.filter(user=user, date=datetime.date.today()).prefetch_related('memo_set')
        
        datas = [{
            'id'     : expense.id,
            'date'   : str(expense.date),
            'expense': expense.detail_expense,
            'memo'   : expense.memo_set.get(expense=expense).content
            } for expense in expenses]
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data'], datas)
    
    def test_history_get_wrongdate(self):
        user    = User.objects.get(id=2)
        headers = {'HTTP_AUTHORIZATION': tokenmaker(user.id, True)}
        date    = str(datetime.date.today() + datetime.timedelta(days=1)).replace('-', '')

        response = client.get('/account/history/'+ date, content_type='application/json', **headers)
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "INVALID_DATE"})

    def test_history_patch_success(self):
        user    = User.objects.get(id=1)
        headers = {'HTTP_AUTHORIZATION': tokenmaker(user.id, True)}
        data = {
                'expenseId': 2,
                'date'     : str(datetime.date.today()),
                'expense'  : 20000,
                'memo'     : 'none'
                }

        response = client.patch('/account/history', json.dumps(data), content_type='application/json', **headers)
        
        newaccount = AccountHistory.objects.get(id=2)
        newmemo    = Memo.objects.get(expense = newaccount)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "SUCCESS"})

        self.assertTrue(data == {'expenseId': newaccount.id,
                                'date'      : str(newaccount.date),
                                'expense'   : newaccount.detail_expense,
                                'memo'      : newmemo.content})
        
    def test_history_patch_keyerror(self):
        user    = User.objects.get(id=1)
        headers = {'HTTP_AUTHORIZATION': tokenmaker(user.id, True)}
        data = {
                'date'    : str(datetime.date.today()),
                'expense' : 20000,
                'memo'    : 'none'
                }

        response = client.patch('/account/history', json.dumps(data), content_type='application/json', **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "KEYERROR"})

    def test_history_patch_wrongId(self):
        user    = User.objects.get(id=1)
        headers = {'HTTP_AUTHORIZATION': tokenmaker(user.id, True)}
        data = {
                'expenseId': 6,
                'date'     : str(datetime.date.today()),
                'expense'  : 20000,
                'memo'     : 'none'
                }

        response = client.patch('/account/history', json.dumps(data), content_type='application/json', **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "BADREQUEST"})
    
    def test_history_patch_nochange(self):
        user    = User.objects.get(id=1)
        headers = {'HTTP_AUTHORIZATION': tokenmaker(user.id, True)}
        data    = {'expenseId' : 2}

        response = client.patch('/account/history', json.dumps(data), content_type='application/json', **headers)
        
        accountobj = AccountHistory.objects.get(id=2)
        origin = {'date'    : datetime.date.today() + datetime.timedelta(days=1),
                  'expense' : 10000,
                  'memo'    : '2'}
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "SUCCESS"})
        self.assertTrue(origin == {
                                    'date'    : accountobj.date,
                                    'expense' : accountobj.detail_expense,
                                    'memo'    : Memo.objects.get(expense=accountobj).content
            })

    def test_history_delete_success(self):
        user    = User.objects.get(id=1)
        headers = {'HTTP_AUTHORIZATION': tokenmaker(user.id, True)}
        
        response = client.delete('/account/history/1', content_type='application/json', **headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "SUCCESS"})
        self.assertFalse(AccountHistory.objects.filter(id=1).exists())

    def test_history_delete_wrongId(self):
        user    = User.objects.get(id=1)
        headers = {'HTTP_AUTHORIZATION': tokenmaker(user.id, True)}

        response = client.delete('/account/history/7', content_type='application/json', **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "BADREQUEST"})

