import jwt

from django.conf import settings

from django.contrib.auth import get_user_model

from rest_framework import exceptions

from django.utils.deprecation import MiddlewareMixin


class CustomMiddleware(MiddlewareMixin):

    def authenticate(self, request, user_id):

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

        try:
            user = User.objects.get(id=user_id)

        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('User does not exist')

        if user is None:
            raise exceptions.AuthenticationFailed('User not found')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('User is inactive')

        self.enforce_csrf(request)

        return (user, None)
