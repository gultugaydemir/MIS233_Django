from django.shortcuts import render, redirect
from .models import Heroes, Items, Buildings, Events
from .forms import WeeklyPollsForm


def home(request):
    return render(request, 'dotabase/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'dotabase/about.html', {'title': 'About'})

def new_to_game(request):
    return render(request, 'dotabase/new_to_game.html', {'title': 'New to Dota2?'})

def esports(request):
    return render(request, 'dotabase/esports.html', {'title': 'E-Sports'})

def heroes(request):
    context = {
        'heroes': Heroes.objects.all()
    }
    return render(request, 'dotabase/heroes.html', context)

def items(request):
    context = {
        'items': Items.objects.all()
    }
    return render(request, 'dotabase/items.html', context)

def buildings(request):
    context = {
        'buildings': Buildings.objects.all()
    }
    return render(request, 'dotabase/buildings.html', context)

def events(request):
    context = {
        'events': Events.objects.all()
    }
    return render(request, 'dotabase/events.html', context)

def runes(request):
    return render(request, 'dotabase/runes.html', {'title': 'Runes'})

def creeps(request):
    return render(request, 'dotabase/creeps.html', {'title': 'Creeps'})

def weeklypoll(request):

    if request.method == 'POST':
        form = WeeklyPollsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/thankyou')

    form = WeeklyPollsForm()
    return render(request, 'dotabase/form.html', {'form': form})

def thankyou(request):
    return render(request, 'dotabase/thankyou.html', {'title': 'Thank you!'})

# Create your views here.
