from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'dotabase/home.html', context)

def about(request):
    return render(request, 'dotabase/about.html', {'title': 'About'})

def new_to_game(request):
    return render(request, 'dotabase/new_to_game.html', {'title': 'New to Dota2?'})

# Create your views here.
