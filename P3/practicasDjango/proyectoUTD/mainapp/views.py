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
        'content':'somos un eequipo de desarrollo de SW'
    })

def mision(request):
    return render(request, 'mainapp/mision.html',{
        'title':'mision',
        'content':'Mision de la empresa'
    })

def vision(request):
    return render(request, 'mainapp/vision.html',{
        'title':'mision',
        'content':'La vision de la empresa'
    })

