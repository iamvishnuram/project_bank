from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name="index"),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('user', views.user, name='user'),
    path('join', views.join, name='join'),
    path('success', views.success, name='success'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
]


