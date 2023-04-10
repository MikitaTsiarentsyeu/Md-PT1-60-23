from django.shortcuts import render, redirect
import datetime
import time
from django.http import HttpResponse, HttpResponseNotFound
from .models import Author, Post
from app.forms import forms

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

def add_post(request):

    if request.method == "POST":
        # form = forms.AddPost(request.POST, request.FILES)
        form = forms.AddPostModelForm(request.POST, request.FILES)

        if form.is_valid():
            post_entry = form.save(commit=False)
            # post_entry = Post()
            # post_entry.title = form.cleaned_data['title']
            # post_entry.subtitle = form.cleaned_data['subtitle']
            # post_entry.content = form.cleaned_data['content']
            # post_entry.post_type = form.cleaned_data['post_type']
            # post_entry.image = form.cleaned_data['image']
            post_entry.issued = datetime.datetime.now()
            post_entry.author = Author.objects.all()[0] #not final version, will be modified

            post_entry.save()
            form.save_m2m()

            return redirect('post', post_entry.id)
    else:
        # form = forms.AddPost()
        form = forms.AddPostModelForm

    return render(request, 'add_post.html', {'form':form})
