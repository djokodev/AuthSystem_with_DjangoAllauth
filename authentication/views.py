from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.models import User

def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            return render(request, 'login.html', {'error': 'Veuillez remplir tous les champs.'})
        
        try:
            user = authenticate(request, username=email, password=password, backend='django.contrib.auth.backends.ModelBackend')
        except:
            return print("Erreur d'authentification de l'utilisateur ", email)

        if user is not None:
           login(request, user, backend='django.contrib.auth.backends.ModelBackend')
           return redirect('home')
        else:
           user = User.objects.create(username=email, email=email, password=password)
           if user:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('home')

    return render(request, "login.html")

@login_required
def home(request):
    context = {"email": request.user.email}
    return render(request, "home.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")