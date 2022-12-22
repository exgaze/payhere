from django.urls import path
from .views      import AccountListView, AccountHistoryView

urlpatterns = [
        path('/list',              AccountListView.as_view()),
        path('/history',           AccountHistoryView.as_view()),
        path('/history/<str:num>', AccountHistoryView.as_view())
        ]
