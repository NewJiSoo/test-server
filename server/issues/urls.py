from django.urls import path, include
from .views import (CreatePostAPIView,
                    PostListView,
                    PostView,

                    )
urlpatterns = [
    path("", PostListView.as_view(), name="list_post"),
    path("<int:pk>/", PostView.as_view(), name="detail_post"),
    path("<int:pk>/view/", PostView.as_view(), name="detail_post_view"),
    path("create/", CreatePostAPIView.as_view(), name="create_post"),
]
