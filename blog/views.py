from django.shortcuts import redirect, render
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    blogs = Blog.objects

    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})