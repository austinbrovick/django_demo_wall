from django.shortcuts import render, redirect
from .models import Post, Comment

# Create your views here.

def wall(request):
    print request.POST
    try:
      request.session['username']
    except:
      request.session['username'] = request.POST['username']
    # print request.session['username']

    posts = Post.objects.all().order_by('-createdAt')
    comments = Comment.objects.all()
    context = {
      "posts" : posts,
      "comments" : comments,
    }
    print posts
    return render(request, 'wall/wall.html', context)

def create_post(request):
    Post.objects.create(creator=request.session['username'], post=request.POST['post'])
    print("hello")
    print request.POST['post']
    return redirect('/wall/enter')

def comment(request, post):
    post1 = Post.objects.get(id=post)
    creator = request.session['username']
    comment_text = request.POST['comment']
    comment = Comment.objects.create(creator=creator, comment=comment_text, post=post1)
    return redirect('/wall/enter')

