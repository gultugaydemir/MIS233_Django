from django.shortcuts import render
from .models import Heroes, Items
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

def talents(request):
    return render(request, 'dotabase/talents.html', {'title': 'Talents'})

def events(request):
    return render(request, 'dotabase/events.html', {'title': 'Events'})

def patches(request):
    return render(request, 'dotabase/patches.html', {'title': 'Patches'})

def creeps(request):
    return render(request, 'dotabase/creeps.html', {'title': 'Creeps'})

def weeklypoll(request):

    if request.method == 'POST':
        form = WeeklyPollsForm(request.POST)
        if form.is_valid():
            form.save()



    form = WeeklyPollsForm()
    return render(request, 'dotabase/form.html', {'form': form})

# Create your views here.
