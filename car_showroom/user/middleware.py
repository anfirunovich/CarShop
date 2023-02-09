import jwt

from django.conf import settings

from django.contrib.auth import get_user_model

from rest_framework import exceptions

from django.utils.deprecation import MiddlewareMixin


def simple_middleware(get_response):

    def middleware(request):
        print("Before response")

        response = get_response(request)

        print("After response")
        return response

    return middleware


class CustomMiddleware(MiddlewareMixin):

    def authenticate(self, request):

        User = get_user_model()
        authorization_header = request.headers.get('Authorization')

        if not authorization_header:
            return None
        try:
            access_token = authorization_header.split(' ')[1]
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('access_token expired')

        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing')

        user = User.objects.filter(id=payload['user_id']).first()

        if user is None:
            raise exceptions.AuthenticationFailed('User not found')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('User is inactive')

        self.enforce_csrf(request)

        return (user, None)
