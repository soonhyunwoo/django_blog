from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all() # Post 모델의 모든 데이터를 가져오겠다
    return render(request, "post/index.html", {"post":posts[0]})