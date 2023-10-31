from django.shortcuts import render
from .models import Menu


def menu_view(request):
    if request.method == 'GET':
        dishes = Menu.objects.all()
        return render(request, template_name='menu.html', context={'dishes': dishes})
