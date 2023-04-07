from django.shortcuts import render
import datetime
import time
from django.http import HttpResponse, HttpResponseNotFound
from .models import Author, Post

# Create your views here.
def test(request):
    current = datetime.datetime.now()
    time.sleep(10)
    return render(request, 'testPage.html', {"ct":current})

def test_str(request, post_id):
    print("test str call detected")
    print(type(post_id))
    print(post_id)
    return render(request, 'testPage.html')

def test_int(request, post_id):
    print("test int call detected")
    print(type(post_id))
    print(post_id)
    return render(request, 'testPage.html')

def posts(request):
    # post_list = ''
    # for post in posts:
    #     post_list += f"<li><h1>{post.title}</h1><p>by {post.author.name}</p></li>"

    # response = f"<h1>All posts</h1><ul>{post_list}</ul>"
    # return HttpResponse(response)

    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts':posts})


def post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except:
        return HttpResponseNotFound()
    # response = f"<h1>{post.title}</h1><p>by {post.author.name}</p>"
    # return HttpResponse(response)
    return render(request, 'post.html', {'post':post})