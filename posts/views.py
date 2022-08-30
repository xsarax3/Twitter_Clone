from distutils import errors
from distutils.log import error
from django.shortcuts import render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm (request.POST, request.FILES)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()
            # Redirect to home
            return HttpResponseRedirect('/')
        
        else:
            # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())

    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]
    form = PostForm()

    # Show
    return render(request, 'posts.html',
                {'posts' : posts})

def delete(request, post_id):
    # Find post
    post =Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

def editpost(request, post_id):
    post = Post.objects.get(id=post_id)
    # if request.method == "GET":
    #     posts = Post.objects.get(id=post_id)
    #     return render(request, "editpost.html", {"posts":posts})
    # if the method is post
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
    # If the form is valid
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    # yes save
    # redirect to home
    # no, show error
        else:
            return HttpResponseRedirect(form.errors.as_Json())
    form = PostForm
    return render(request, 'editpost.html',{'post': post, 'form': form} )
    
def like(request, post_id):
    likedtweet = Post.objects.get(id=post_id)
    likedtweet.like += 1
    likedtweet.save()
    return HttpResponseRedirect('/')