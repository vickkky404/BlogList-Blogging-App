from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from blog import models
from .models import Post
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
import math


def calculate_reading_time(text):
    words = len(text.split())
    reading_time = max(1, round(words / 200))
    return reading_time


def calculate_word_count(text):
    return len(text.split())




def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email= request.POST.get('uemail')
        password = request.POST.get('upassword')
        newUser = User.objects.create_user(username=name, email=email, password=password)
        newUser.save()
        return redirect('/loginn')
    return render(request, 'blog/signup.html')




def loginn(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')
        userr = authenticate(request, username=name, password=password)
        if userr is not None:
            login(request, userr)
            return redirect('/home')
        else:
            return redirect('/loginn/')

    return render(request, 'blog/login.html')




def home(request):
    query = request.GET.get('q', '')
    sort = request.GET.get('sort', 'newest')
    
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query) | 
            Q(author__username__icontains=query)
        )
    else:
        posts = Post.objects.all()
    
    if sort == 'oldest':
        posts = posts.order_by('date_posted')
    else:
        posts = posts.order_by('-date_posted')
    
    for post in posts:
        post.word_count = calculate_word_count(post.content)
        post.reading_time = calculate_reading_time(post.content)
        post.preview = post.content[:150] + '...' if len(post.content) > 150 else post.content
    
    total_posts = Post.objects.count()
    total_users = User.objects.count()
    
    context = {
        'posts': posts,
        'search_query': query,
        'sort': sort,
        'total_posts': total_posts,
        'total_users': total_users
    }
    return render(request, 'blog/home.html', context)



def newPost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        npost = models.Post(title=title, content=content, author=request.user)
        npost.save()
        return redirect('/home')
    
    return render(request, 'blog/newpost.html')




def myPost(request):
    context = {
        'posts': Post.objects.filter(author=request.user).order_by('-date_posted')
    }
    return render(request, 'blog/mypost.html', context)


def editPost(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        
        if post.author != request.user:
            return redirect('/mypost')
        
        if request.method == 'POST':
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.save()
            return redirect('/mypost')
        
        context = {'post': post}
        return render(request, 'blog/editpost.html', context)
    except Post.DoesNotExist:
        return redirect('/mypost')


def deletePost(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        
        if post.author != request.user:
            return redirect('/mypost')
        
        post.delete()
        return redirect('/mypost')
    except Post.DoesNotExist:
        return redirect('/mypost')


def signout(request):
    logout(request)
    return redirect('/loginn')

