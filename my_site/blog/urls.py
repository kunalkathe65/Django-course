from django.conf.urls import url
from django.urls import path
from blog import views

urlpatterns = [
    path("", views.starting_page, name="starting_page"),
    path("/posts", views.posts_page, name="posts_page"),
    path("/posts/<slug:slug>", views.post_detail_page, name="post_detail_page")
]
