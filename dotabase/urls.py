from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'dotabase-home'),
    path('about/', views.about, name = 'dotabase-about'),
    path('new_to_game/', views.new_to_game, name = 'dotabase-new_to_game'),
    path('esports/', views.esports, name = 'dotabase-esports'),
    path('heroes/', views.heroes, name = 'dotabase-heroes'),
    path('items/', views.items, name = 'dotabase-items'),
    path('talents/', views.talents, name = 'dotabase-talents'),
    path('events/', views.events, name = 'dotabase-events'),
    path('patches/', views.patches, name = 'dotabase-patches'),
    path('creeps/', views.creeps, name = 'dotabase-creeps'),
]