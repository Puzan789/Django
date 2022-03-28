from django.shortcuts import render
from django.http import HttpResponse
from .models import HomePage, Blog
# Create your views here.

def index(request):
    homepage_data = HomePage.objects.all()
    #homepage_data = HomePage.objects.get(id=1)
    context = {
        'title':homepage_data[0].title,
        'para1':homepage_data[0].para1,
        'para2':homepage_data[0].para2,
        'skills_list':homepage_data[0].skills_list,
        'softwares_list':homepage_data[0].softwares_list,
        'mail':homepage_data[0].mail,
    }
    return render(request, "pages/index.html",context)

def contact(request):
    #return HttpResponse("Hello, world. You're at the portfolio contact.")
    return render(request, "pages/contact.html")

def blog(request):
    blogs_list = Blog.objects.all()

    context = {
        'blogs_list':blogs_list,
    }
    
    return render(request, "blogs/blogs.html",context)

def blog_detail(request,id):
    #blogs_list = Blog.objects.all()
    # for blog in blogs_list:
    #     if blog['id'] == int(id):
    #         context = {
    #             'blog':blog,
    #         }
    blog = Blog.objects.get(id=id)
    context = {
        'blog': blog
    }
    return render(request, "blogs/blog_detail.html",context)
