from django.urls import path
from favourites.views import (
    likes, delete_likes
)

urlpatterns = [
    path('likes/', likes, name='likes'),
    path('delete/likes/', delete_likes, name='del-likes'),
]