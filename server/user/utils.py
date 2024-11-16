import jwt
from django.conf import settings
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response


# 사용자 인스턴스(user)를 받아서 JWT 액세스 토큰 생성
def generate_access_token(user):
    payload = {
        'user_id': user.id,
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')


# 토큰 유효성 검증 및 payload를 디코딩
def decode_access_token(access_token):
    try:
        payload = jwt.decode(
            access_token, settings.SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']

    # 토큰이 만료된 경우 발생
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Token has expired, please log in again')

    # 토큰이 유효하지 않은 경우 발생
    except jwt.InvalidTokenError:
        raise AuthenticationFailed('Invalid token, please log in again')
