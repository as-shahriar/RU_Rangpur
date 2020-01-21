from django.contrib import admin
from django.urls import path
from ru import views
urlpatterns = [
    path('logout', views.logout_view, name='logout'),
    path('profile', views.profile, name='profile'),
    path('delete', views.delete_view, name='delete'),
    path('login', views.login_view, name='login'),
    path('signup', views.signup_view, name='signup'),
    path('', views.home, name='home')
]
