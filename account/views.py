import json
import datetime
import requests

from django.http  import JsonResponse
from django.views import View
from collections  import defaultdict

from user.utils import login_decorator
from .models    import Memo, AccountHistory

class AccountListView(View):
    @login_decorator
    def get(self, request):
        user     = request.user
        expenses = AccountHistory.objects.filter(user=user)
        
        expenselist = defaultdict(int)
        for expense in expenses:
            expenselist[str(expense.date)] += expense.detail_expense

        result = [{key : value} for key, value in expenselist.items()]
        return JsonResponse({"data": result, "message": "SUCCESS"}, status = 200)
    

class AccountHistoryView(View):
    @login_decorator
    def post(self, request):
        try:
            data    = json.loads(request.body)
            user    = request.user
            datestr = data['date'].split('-')
            date    = datetime.date(int(datestr[0]), int(datestr[1]), int(datestr[2]))
            expense = int(data['expense'])
            content = data['memo']

            account = AccountHistory.objects.create(
                        user = user,
                        date = date,
                        detail_expense = expense
                    )
            Memo.objects.create(expense = account, content = content)

            return JsonResponse({"message": "SUCCESS"}, status = 200)

        except KeyError:
            return JsonResponse({"message": "KEYERROR"}, status = 400)

    @login_decorator
    def get(self, request, num):
        user     = request.user
        date     = datetime.date(int(num[:4]), int(num[4:6]), int(num[6:]))
        expenses = AccountHistory.objects.filter(user = user, date = date).prefetch_related('memo_set')

        if not expenses:
            return JsonResponse({"message": "INVALID_DATE"}, status = 400)

        result = [{
                'id'      : expense.id,
                'date'    : str(expense.date),
                'expense' : expense.detail_expense,
                'memo'    : expense.memo_set.get(expense=expense).content
                } for expense in expenses]
            
        return JsonResponse({"data": result, "message": "SUCCESS"}, status = 200)

    @login_decorator
    def patch(self, request):
        try:
            user         = request.user
            data         = json.loads(request.body)
            expense_id   = data['expenseId']
            accountobj   = AccountHistory.objects.get(id = expense_id, user=user)
            expense_date = data.get('date', accountobj.date)
            expense      = data.get('expense', accountobj.detail_expense)
            content      = data.get('memo', accountobj.memo_set.get(expense = accountobj).content)
            
            if type(expense_date) == str:
                datestr      = expense_date.split('-')
                expense_date = datetime.date(int(datestr[0]), int(datestr[1]), int(datestr[2]))
            
            accountobj.detail_expense = expense
            accountobj.date           = expense_date
            accountobj.save()
            
            memoobj         = accountobj.memo_set.get(expense = accountobj)
            memoobj.content = content
            memoobj.save()
            
            return JsonResponse({"message": "SUCCESS"}, status = 200)

        except KeyError:
            return JsonResponse({"message": "KEYERROR"}, status = 400)
        
        except AccountHistory.DoesNotExist:
            return JsonResponse({"message": "BADREQUEST"}, status = 400)
            
    @login_decorator
    def delete(self, request, num):
        try:
            user = request.user
            
            AccountHistory.objects.get(id = num, user=user).delete()

            return JsonResponse({"message": "SUCCESS"}, status = 200)

        except AccountHistory.DoesNotExist:
            return JsonResponse({"message": "BADREQUEST"}, status = 400)

