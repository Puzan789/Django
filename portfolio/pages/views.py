from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You're at the portfolio index.")
    return render(request, "pages/index.html")

def contact(request):
    #return HttpResponse("Hello, world. You're at the portfolio contact.")
    return render(request, "pages/contact.html")

def blog(request):
   
    return render(request, "blogs/blogs.html")

def blog_detail(request):
    return render(request, "blogs/blog_detail.html")

def blogdetailjava(request):
    return render(request, "blogs/blogdetailjava.html")
def blogdetailc(request):
    return render(request, "blogs/blogdetailc.html")