from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'dotabase-home'),
    path('about/', views.about, name = 'dotabase-about'),
    path('new_to_game/', views.new_to_game, name = 'dotabase-new_to_game'),
]