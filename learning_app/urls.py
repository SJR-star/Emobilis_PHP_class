# import path from django.urls
from django.urls import path
from . import views

# app_name

urlpatterns = [
    path('home/', views.Welcome_home, name="home"),# home url
    path('about/', views.about_us, name="about"),
    path('story/', views.Our_story, name="story"),
    path('team/', views.Our_team_members, name="team_members"),
    path('contact/', views.Contact_Us, name="contact" )
]