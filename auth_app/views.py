import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


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
            logger.error("Auth failed. Invalid password")
            return render(request, 'auth_app/auth_page.html')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            logger.info("Successful auth of " + user.username)
            return redirect('home')

        # Render the login page template (GET request)

    return render(request, 'auth_app/auth_page.html')


@login_required
def log_out(request):
    user = request.user
    logout(request)
    logger.info("Successful logout of " + user.username)
    return redirect('auth_page')

