from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.login, name='login'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('profile_index', views.profile_index, name='profile_index'),
    path('profile_book', views.profile_book, name='profile_book'),
    path('profile_cars', views.profile_cars, name='profile_cars'),
    path('profile_customer', views.profile_customer, name='profile_customer'),
    path('profile_return', views.profile_return, name='profile_return')
]
