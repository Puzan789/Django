from django.urls import path

from .views import  contact, index, blog, blog_detail

urlpatterns = [
    path("", index, name="index"),
    path("contact/", contact, name="contact"),
    path("blog/", blog, name="blog"),
   path('blog_detail/<int:id>', blog_detail, name="blog_detail"),
]