from django.contrib import admin
from django.urls import path
from search import views
import os
urlpatterns = [
    path('search/', views.search, name='search'),
    path('report/', views.report, name='report'),
    path('user/<slug:slugtxt>', views.other_profile, name='other_profile'),
    path('about/', views.about, name='about'),
    path('password-reset/', views.pass_reset, name='reset'),
    path('password-reset/<username>', views.input_password, name='input_password'),
    path('table/', views.show_all, name='table'),
    path('error/', views.error_page, name='error'),
    path('teachers/', views.see_teachers, name='teachers'),
    path('students/', views.see_students, name='students'),
    path('alumni/', views.see_alumni, name='alumni'),
    path('download/', views.download, name='download'),

]
handler404 = views.handler404
