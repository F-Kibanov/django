from django.urls import path
from . import views

urlpatterns = [
    path('/games/', views.choice_game_type, name='games'),
    path('/add_author/', views.add_author, name='add_author'),
    path('/add_post/', views.add_post, name='add_post'),
    path('/upload/', views.upload_image, name='upload_image'),
]
