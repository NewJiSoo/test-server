from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token

            res = Response({
                "user": serializer.data,
                "message": "회원가입이 완료되었습니다.",
                "refreshToken": str(refresh),
                "accessToken": str(access),
            }, status=status.HTTP_201_CREATED)

            # res.set_cookie("refreshToken", str(refresh), httponly=True)
            # res.set_cookie("accessToken", str(access), httponly=True)
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get("user")
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token

            # Return tokens in response
            res = Response({
                "refreshToken": str(refresh),
                "accessToken": str(access),
            }, status=status.HTTP_200_OK)

            # Set tokens as cookies
            # res.set_cookie("refreshToken", str(refresh), httponly=True)
            # res.set_cookie("accessToken", str(access), httponly=True)
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
