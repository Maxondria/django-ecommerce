from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import redirect, render

from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {"title": "Home Page"}
    return render(request, "home_page.html", context)


def about_page(request):
    context = {"title": "About Page"}
    return render(request, "home_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "content": "Welcome to the contact page.",
        "form": contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)

    context = {"title": "Login Page", "form": form}

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            print(user.is_authenticated)
            return redirect("home")
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
