from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def auth_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return render(request, 'auth_app/auth_page.html')

            # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)

        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return render(request, 'auth_app/auth_page.html')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('home')

        # Render the login page template (GET request)

    return render(request, 'auth_app/auth_page.html')


@login_required
def log_out(request):
    logout(request)
    return redirect('auth_page')

