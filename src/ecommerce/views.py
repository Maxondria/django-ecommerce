from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import LoginForm


def login_page(request):
    form = LoginForm(request.POST or None)

    context = {"title": "Login Page", "form": form}

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            print(user.is_authenticated())
            return redirect("login/")
    return render(request, "auth/login.html", context)


def register_page(request):
    pass
