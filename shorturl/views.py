import json
import datetime
import requests
import pyshorteners

from django.http import JsonResponse, HttpResponseRedirect
from django.views import View

from user.utils import login_decorator
from .models import ShortURL

class URLShortnerView(View):
    @login_decorator
    def post(self, request):
        try:
            user_id = request.user.id
            data    = json.loads(request.body)
            urlpath = data['url']

            shortner = pyshorteners.Shortener()

            surlori = shortner.chilpit.short(urlpath + str(user_id))
            surl    = surlori[16:]
            
            if ShortURL.objects.filter(urlshorten=surl, valid=True).exists():
                returnurl = 'http://chilp.it/' + ShortURL.objects.get(urlorigin=urlpath, valid=True).urlshorten
                return JsonResponse({"data": returnurl, "message": "SUCCESS"}, status = 200)
            
            ShortURL.objects.create(urlorigin = urlpath, urlshorten = surl)
    
            return JsonResponse({"data": surlori, "message": "SUCCESS"}, status = 200)

        except KeyError:
            return JsonResponse({"message": "KEYERROR"}, status = 400)


class RedirectView(View):
    def get(self, request, url):
        urlobj = ShortURL.objects.get(urlshorten = url)
        
        if urlobj.valid == False:
            return JsonResponse({"message": "URLEXPIRED"}, status = 400)

        diff = datetime.datetime.now() - urlobj.created_at
            
        if diff.seconds / 60 > 30:
            urlobj.valid = False
            urlobj.save()
            return JsonResponse({"message": "URLEXPIRED"}, status = 400)
            
        return HttpResponseRedirect(urlobj.urlorigin)

