from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Post
from .serializers import CreatePostSerializer, PostListSerializer, PostDetailSerializer
from django.db import transaction
import datetime
from django.utils import timezone


# post 리스트
class PostListView(APIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def get(self, request):
        post = Post.objects.all()
        serializer = PostListSerializer(instance=post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# post detail
class PostView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        try:
            post = get_object_or_404(Post, pk=pk)
            serializer = PostDetailSerializer(post)
            response = Response(serializer.data, status=status.HTTP_200_OK)

            # 조회수 증가 로직
            tomorrow = timezone.datetime.replace(
                timezone.datetime.now(), hour=23, minute=59, second=0)
            expires = datetime.datetime.strftime(
                tomorrow, "%a, %d-%b-%Y %H:%M:%S GMT")
            user_id = request.user.id if request.user.is_authenticated else None

            if user_id:
                user_cookie_key = f'user_{user_id}_hit'

                if request.COOKIES.get(user_cookie_key) is not None:
                    cookies = request.COOKIES.get(user_cookie_key)
                    cookies_list = cookies.split("|")
                    if str(pk) not in cookies_list:
                        response.set_cookie(
                            user_cookie_key,
                            cookies + f'|{pk}',
                            expires=expires,
                            samesite='None',
                            httponly=True,
                            secure=True
                        )
                        with transaction.atomic():
                            post.views += 1
                            post.save()
                else:
                    # 쿠키가 없는 경우, 새로 생성해서 해당 게시물 번호를 저장
                    response.set_cookie(user_cookie_key, f'{pk}', expires=expires,
                                        samesite='None',
                                        secure=True,
                                        httponly=True
                                        )
                    post.views += 1
                    post.save()

            return response
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CreatePostAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)
