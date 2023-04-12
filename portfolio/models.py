from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    summary = models.CharField(max_length=255)
    adventure_date = models.DateField()
    published = models.DateTimeField(default=datetime.now)
    likes = models.ManyToManyField(User, related_name='blog_post')


    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    

    #need a redirect for when you create a post on the website
    def get_absolute_url(self):
        return reverse('article_detail', args=(str(self.id),))
