from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Panier, Produit
from .forms import LoginForm
from .forms import RegisterForm
from django.contrib.auth import logout
from django.contrib.auth.models import User


def index(request):
    data = Produit.objects.all()
    produit = {'produit': data}
    return render(request, "e_commerce/index.html", produit)
def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            data = Produit.objects.all()
            produit = {'produit': data}
            return render(request, "e_commerce/index.html", produit)
        else:
            form = LoginForm()
            error_message = 'Identifiants invalides'
            context = {'form': form, 'error_message': error_message}
            return render(request, "e_commerce/connexion.html", context)
    else:
        form = LoginForm()
        context = {'form': form}
        return render(request, 'e_commerce/connexion.html', context)

def logout_view(request):
    logout(request)
    data = Produit.objects.all()
    produit = {'produit': data}
    return render(request, "e_commerce/index.html", produit)

def inscription(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            User.objects.create_user(username=username, password=password)
            return HttpResponseRedirect('/e_commerce/connexion/')
        else:
            form = RegisterForm()
            error_message = 'Identifiants invalides'
            context = {'form': form, 'error_message': error_message}
            return render(request, "e_commerce/inscription.html", context)
    else:
        form = RegisterForm()
        context = {'form': form}
        return render(request, "e_commerce/inscription.html", context)

def panier(request):
    return render(request, "e_commerce/panier.html")

def achat(request, pk):
    print('test')
    Panier.objects.create(produit_id=pk, user_id=request.user.id)
    return HttpResponseRedirect('/e_commerce/')
