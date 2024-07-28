from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .tasks import test_task


def get_user_data(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    return email, password


def validate_login_form(email, password):
    if not email or not password:
        return 'Veuillez remplir tous les champs.'
    try:
        validate_email(email)
    except ValidationError:
        return 'Veuillez entrer une adresse email valide.'

    return None


def login_user(request, user, backend='django.contrib.auth.backends.'
               '                        ModelBackend'):
    login(request, user, backend=backend)
    return redirect('home')


def create_user(email, password):
    user = User.objects.create_user(username=email,
                                    email=email,
                                    password=password)
    return user


def loginView(request):
    if request.method == 'POST':
        email, password = get_user_data(request)
        error_login_form = validate_login_form(email, password)
        if error_login_form:
            return render(request, 'login.html', {'error': error_login_form})
        try:
            user = authenticate(request,
                                username=email,
                                password=password,
                                backend='django.contrib.auth.backends.'
                                'ModelBackend')
        except Exception as e:
            return render(request, 'login.html',
                          {'error': f"Erreur d'authentification : {str(e)}"})

        if user is not None:
            test_task.delay()
            return login_user(request, user)
        else:
            user = create_user(email, password)
            return login_user(request, user)
    return render(request, "login.html")


@login_required
def home(request):
    context = {"email": request.user.email}
    return render(request, "home.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")
