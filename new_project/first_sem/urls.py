from django.urls import path
from . import views


urlpatterns = [
    path('/hello/', views.hello, name='hello'),
    path('/about/', views.about, name='about'),
    path('/coin/', views.coin, name='coin'),
    path('/dice/', views.dice, name='dice'),
    path('/hundred/', views.hundred, name='hundred'),
    path('/main/', views.main, name='main'),
    path('/about_me/', views.about_me, name='about_me'),
]
