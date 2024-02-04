from django.shortcuts import render
from .models import Submenu

from .models import MainMenu

# Create your views here.
def main_menu_display(request):
    return render(request, 'Menu/index.html', {'menu': MainMenu.objects.all()})


def submenu_display(request, path):   
    return render(request, 'Menu/index.html', {'main_menu': path})