from django.urls import path
from . import views
from .views import post


urlpatterns = [
    path('/coin/<int:count>', views.coin, name='coin'),
    path('/dice/<int:count>', views.dice, name='dice'),
    path('/hundred/<int:count>', views.hundred, name='hundred'),
    path('/author/', views.authors_view, name='author'),
    path('/posts/', views.post_view, name='posts'),
    path('/author_posts/<int:author_id>', views.author_posts, name='author_posts'),
    path('/post/<int:post_id>', views.post, name='post'),
    path('/get_client_orders/<int:client_id>', views.get_client_orders, name='get_client_orders'),
]
