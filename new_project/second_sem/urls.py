from django.urls import path
from . import views


urlpatterns = [
    path('/coin/', views.coin, name='coin'),
    path('/authors/', views.authors_view, name='authors'),
    path('/post/', views.post_view, name='post'),
    path('/get_orders/', views.get_orders, name='get orders'),
]
