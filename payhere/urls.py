from django.urls    import path, include
from shorturl.views import URLShortnerView, RedirectView

urlpatterns = [
    path('user',               include('user.urls')),
    path('account',            include('account.urls')),
    path('short',              URLShortnerView.as_view()),
    path('chilp.it/<str:url>', RedirectView.as_view())
]
