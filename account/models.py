from django.db import models

class Memo(models.Model):
    expense    = models.ForeignKey('AccountHistory', on_delete = models.CASCADE)
    content    = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'memo'

class AccountHistory(models.Model):
    user           = models.ForeignKey('user.User', on_delete = models.CASCADE)
    date           = models.DateField()
    detail_expense = models.IntegerField()
    created_at     = models.DateTimeField(auto_now_add = True)
    updated_at     = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'accounthistory'


