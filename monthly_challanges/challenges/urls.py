from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month>", views.show_challenge_by_number),
    path("<str:month>", views.show_challenge, name="challengeURL")
]
