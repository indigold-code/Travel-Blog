from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from datetime import datetime, date

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    summary = models.CharField(max_length=255)
    adventure_date = models.DateField()
    published = models.DateTimeField(default=datetime.now)
    

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    

    #need a redirect for when you create a post on the website
    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.id)))
