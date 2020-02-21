from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import redirect, render

from .forms import LoginForm, RegisterForm


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


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)

    context = {"title": "Login Page", "form": form}

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")

        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        print(user)
    return render(request, "auth/register.html", context)
