from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'users/profile.html', {'user': user})


def user_login(request):
    if request.method == 'POST':
        # Form submission, process login
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Authentication successful, log in the user
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard page after login
        else:
            # Authentication failed, display error message
            error_message = "Invalid username or password."
            return render(request, 'user_login.html', {'error_message': error_message})
    else:
        # GET request, render the login form
        return render(request, 'user_login.html')


def user_register(request):
    if request.method == 'POST':
        # Form submission, process registration
        # Retrieve form data
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        # Additional form validation and user creation logic
        # Assuming you have a User model for user registration
        user = User.objects.create_user(username=username, email=email, password=password)
        # Additional user profile creation logic if needed
        return redirect('login')  # Redirect to the login page after successful registration
    else:
        # GET request, render the registration form
        return render(request, 'user_register.html')


def user_settings(request):
    if request.method == 'POST':
        # Form submission, process settings update
        # Retrieve form data and update user settings
        # Redirect to appropriate page after settings update
        pass
    else:
        # GET request, render the settings form
        return render(request, 'user_settings.html')