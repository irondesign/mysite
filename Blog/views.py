from django.shortcuts import render
from Blog.models import Posts
# Create your views here.

def index(request):
    posts = Posts.objects.all()
    args = {}
    args['posts']=posts
    return render(request, 'index.html', args)