
from django.urls import path
from .views import HomeView, ArticleDetailView, home, AddPostView, LikeView

urlpatterns = [
    path('', home, name='home'),
    path('travelblog', HomeView.as_view(), name='blog'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('addpost/', AddPostView.as_view(), name='addpost'),
    path('like/<int:pk>', LikeView, name='like_post'),
]
