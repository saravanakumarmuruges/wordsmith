from django.shortcuts import render
from django.http import HttpResponse
from .models import blogs

def blog(request):
    data = blogs.objects.all()
    return render(request, 'blogs/blogs.html', {'data' : data})

def blog_posts(request, id):
    data = blogs.objects.get(pk=id)
    return render(request, 'blogs/blog_post.html',
                  {'title':data.title, 
                   'author': data.author_name,
                   'genre':data.genre,
                   'created_time':data.created_time,
                   'content':data.content})