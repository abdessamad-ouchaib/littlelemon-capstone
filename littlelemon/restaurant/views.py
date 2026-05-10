from django.shortcuts import render
from .models import Menu


def index(request):
    return render(request, 'restaurant/index.html', {})


def about(request):
    return render(request, 'restaurant/about.html', {})


def menu(request):
    menu_data = Menu.objects.all()
    main_data = {'menu': menu_data}
    return render(request, 'restaurant/menu.html', main_data)


def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ''
    return render(request, 'restaurant/menu_item.html', {'menu_item': menu_item})
