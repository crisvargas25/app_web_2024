from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from articulos.models import *

# Create your views here.
@login_required(login_url='index')
def lista_art(request):

    #Sacar los articulos de la BD
    articulos = Article.objects.all()

    return render(request, 'articulos/listado_art.html', {
        'title': 'Artículos',
        'content': 'Listado de artículos',
        'article': articulos
    })

@login_required(login_url='index')
def lista_cat(request):

    #Sacar las categorias de la BD
    categorias = Category.objects.all()

    return render(request, 'categorias/listado_cat.html', {
        'title': 'Categorías',
        'content': 'Listado de categorías',
        'category': categorias
    })