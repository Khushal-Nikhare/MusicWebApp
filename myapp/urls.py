from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("song/",views.get_song,name="get_song"),
    path("artist/<str:artist>",views.artist,name="artist"),
    path("playlist/<str:playlist>",views.playlist,name="playlist"),
]
