from django.shortcuts import render,HttpResponse,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from mainapp.forms import RegisterForm

# Create your views here.

def index (request):
    mensaje="Hola soy un mensaje"
    return render(request,'mainapp/index.html',{
        'title':'Inicio',
        'content':'.:: !Bienvendido a la pagina principal!::.',
        'mensaje':mensaje
    })

@login_required(login_url='inicio')
def about(request):
    return render(request, 'mainapp/about.html',{
        'title':"Acerca de nosotros",
        'content':'Soy un examen'
    })


@login_required(login_url='inicio')
def mision(request):
    return render(request, 'mainapp/mision.html',{
        'title':'Vision',
        'content':'Mision de la empresa'
    })

@login_required(login_url='inicio')
def vision(request):
    return render(request, 'mainapp/vision.html',{
        'title':'mision',
        'content':'La vision de el examen'
    })

def registro(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        register_form = RegisterForm()
        if request.method == "POST":
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                messages.success(request, "Registro completado con éxito.")
                return redirect('inicio')
        return render(request, 'users/registro.html', {
            'title': 'Registro de Usuarios',
            'register_form': register_form
        })

def login_user(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request, "Bienvenido al Inicio de sesion")
                return redirect('inicio')
            else:
                messages.warning(request, "Credenciales incorrectas")
        return render(request, 'users/login.html',{
            'title':'Login',
            'content':'Inicia sesion ahora'
        })


def page404(request, exception):
    return render(request, 'mainapp/error404.html')

def logout_user(request):
    logout(request)
    return redirect('inicio')