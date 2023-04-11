
from django.urls import path
from .views import HomeView, ArticleDetailView, home, AddPostView

urlpatterns = [
    path('', home, name='home'),
    path('travelblog', HomeView.as_view(), name='blog'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('addpost/', AddPostView.as_view(), name='addpost'),
]
