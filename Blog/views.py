from django.shortcuts import render, redirect
from Blog.models import Posts
from Blog.models import Pages
from Blog.forms import AddNewsForm

# Create your views here.

def index(request):
    posts = Posts.objects.order_by('-date')
    pages = Pages.objects.all()
    args = {}
    args['pages']=pages
    args['posts']=posts
    return render(request, 'index.html', args)

def pages(request, page_slug):
    menupage = Pages.objects.all()
    pages = Pages.objects.get(slug=page_slug)
    args = {}
    args['onepage']=pages
    args['pages'] = menupage
    return render(request, 'page.html', args)

def posts(request, post_slug):
    menupage = Pages.objects.all()
    post = Posts.objects.get(slug=post_slug)
    args = {}
    args['onepost']=post
    args['pages']=menupage
    return render(request, 'post.html', args)

def addnews(request):
    args={}
    if request.method == 'POST':
        form = AddNewsForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddNewsForm()
        args['form']=form
        return render(request, 'add_news.html', args)
