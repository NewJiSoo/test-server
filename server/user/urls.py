from django.urls import path
from user.views import (
    RegisterAPIView,
    LoginAPIView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # 로그인, 회원가입
    path('signup/', RegisterAPIView.as_view(), name="signup"),
    path('login/', LoginAPIView.as_view(), name="login"),

    # 토큰 가져오기/리프레시 토큰으로 갱신하기
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
