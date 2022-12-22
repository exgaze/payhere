import json
import bcrypt
import jwt

from django.http            import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from my_settings import SECRET_KEY, ALGORITHM
from user.models import User

def login_decorator(func):
    def wrapper(self, request, *args, **kargs):
        if 'Authorization' not in request.headers:
            return JsonResponse({"message": "NEED_LOGIN"}, status = 400)

        token = request.headers['Authorization']

        try:
            data         = jwt.decode(token, SECRET_KEY, ALGORITHM)
            user         = User.objects.get(id = data['user'])
            request.user = user

        except jwt.DecodeError:
            return JsonResponse({"message": "INVALID_TOKEN"}, status = 400)

        except jwt.ExpiredSignatureError:
            return JsonResponse({"message": "INVALID_TOKEN"}, status = 400)
        
        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status = 400)

        return func(self, request, *args, **kargs)

    return wrapper
