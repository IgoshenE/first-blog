from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_data__lte=timezone.now()).order_by('published_data')
    return render(request, 'blog/post_list.html', {'posts': posts})


def regist(request):
    return render(request, 'blog/104.html')

def main(request):
    return render(request, 'blog/100.html')
def boks(request):
    return render(request, 'blog/102.html')
def video(request):
    return render(request, 'blog/101.html')
def mma(request):
    return render(request, 'blog/103.html')
def otpravleno(request):
    return render(request, 'blog/105.html')


