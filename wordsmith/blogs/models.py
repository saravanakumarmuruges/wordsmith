from django.db import models
from django.shortcuts import reverse

class blogs(models.Model):
    status_li = [(1, 'Active'), (2, 'Inactive'), (3, 'InProgress'), (4, 'EOL')]
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    footer = models.CharField(max_length=100)
    genre = models.CharField(max_length=10)
    author_name = models.CharField(max_length=20)
    created_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=status_li)
    
    def get_absolute_url(self):
        return reverse("blog_post", args=[self.id])
    