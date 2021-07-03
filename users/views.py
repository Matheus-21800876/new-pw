from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.


def index_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    return render(request, "users/user.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
                    request,
                    username=username,
                    password=password
        )

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('website:show_contato'))
        else:
            return render(request, 'users/login.html', {
                'message': 'Credenciais inválidas.'
            })

    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {
        'message': 'Logged out'})
