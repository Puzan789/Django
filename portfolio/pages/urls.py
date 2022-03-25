from django.urls import path

from .views import blogdetailc, blogdetailjava, contact, index,blog,blog_detail

urlpatterns = [
    path("", index, name="index"),
    path("contact/", contact, name="contact"),
    path("blog/", blog, name="blog"),
    path('blog_detail/', blog_detail, name="blog_detail"),
    path('blogdetailjava/', blogdetailjava, name="blogdetailjava"),
    path('blogdetailc/', blogdetailc, name="blogdetailc"),

]