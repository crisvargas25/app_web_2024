from django.shortcuts import render

from django.shortcuts import render

# Create your views here.

def index (request):
    mensaje="Hola soy un mensaje"
    return render(request,'mainapp/index.html',{
        'title':'Inicio',
        'content':'.:: !Bienvendido a la pagina principal!::.',
        'mensaje':mensaje
    })

def about(request):
    return render(request, 'mainapp/about.html',{
        'title':"Acerca de nosotros",
        'content':'Soy un examen'
    })

def mision(request):
    return render(request, 'mainapp/mision.html',{
        'title':'Vision',
        'content':'Mision de la empresa'
    })

def vision(request):
    return render(request, 'mainapp/vision.html',{
        'title':'mision',
        'content':'La vision de el examen'
    })

def page404(request, exception):
    return render(request, 'mainapp/404.html', status=404)