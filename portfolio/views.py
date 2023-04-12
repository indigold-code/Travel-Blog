from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))


def home(request):
    return render(request, 'home.html', {})


class HomeView(ListView):
    model = Post 
    template_name = 'travel_blog.html'
    ordering = ['-id']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        post_by_id = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post_by_id.total_likes()

        liked = False
        if post_by_id.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked 

        return context



class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    
    