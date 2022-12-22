import jwt
import re
import bcrypt
import requests
import json
import datetime

from django.conf            import settings
from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError

from my_settings import SECRET_KEY, ALGORITHM
from user.models import User

class SignUpView(View):
    def emailValidator(self, email):
        pattern = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        return pattern.match(email)

    def post(self, request):
        try:
            datas    = json.loads(request.body)
            email    = datas['email']
            password = datas['password']
            
            if not self.emailValidator(email=email):
                return JsonResponse({"message": "INVALID_EMAIL"}, status = 400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({"message": "USER_ALREADY_EXISTS"}, status = 400)

            encodepw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            strpw    = encodepw.decode('utf-8')
            
            User.objects.create(
                    email    = email,
                    password = strpw
                    )
            
            return JsonResponse({"message": "SUCCESS"}, status = 200)

        except KeyError:
            return JsonResponse({"message": 'KEYERROR'}, status = 400)

class SignInView(View):
    def post(self, request):
        try:
            datas    = json.loads(request.body)
            email    = datas['email']
            password = datas['password']

            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)

                if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                    expire = datetime.datetime.now() + datetime.timedelta(days = 1)
                    token  = jwt.encode({'user' : user.id, 'exp': expire}, SECRET_KEY, ALGORITHM)
                    
                    return JsonResponse({"message": "SUCCESS", "access_token": token}, status = 200)
                
                return JsonResponse({"message": "INVALID_PASSWORD"}, status = 400)

            return JsonResponse({"message": "INVALID_EMAIL"}, status = 400)
        
        except KeyError:
            return JsonResponse({"message": "KEYERROR"}, status = 400)

