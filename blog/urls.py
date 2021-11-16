from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blogHome"),
    path("blog_post/<int:id>/", views.blogpost, name="blogHome")
]