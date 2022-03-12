from django.shortcuts import render
from .models import Blog
def posts(request):
    template_name = 'post.html'
    context = {}
    context["posts"] = Blog.objects.all()
    return render(request,template_name,context)