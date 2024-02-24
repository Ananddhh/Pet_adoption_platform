from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserSettingsForm

@login_required
def user_settings(request):
    if request.method == 'POST':
        form = UserSettingsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your settings have been updated successfully.')
            return redirect('user_settings')
    else:
        form = UserSettingsForm(instance=request.user)
    return render(request, 'user_settings.html', {'form': form})


def user_profile(request, username):
    # Retrieve user profile based on username
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
            return redirect('home')  
        else:
            
            error_message = "Invalid username or password."
            return render(request, 'user_login.html', {'error_message': error_message})
    else:
        
        return render(request, 'user_login.html')
    
def user_register(request):
    if request.method == 'POST':
        # Form submission, process registration
        # Retrieve form data
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        # Check if passwords match
        if password != confirm_password:
            error_message = "Passwords do not match."
            return render(request, 'user_register.html', {'error_message': error_message})
        
        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        
        # Redirect to the login page after successful registration
        return redirect('login')
    else:
        # Render the registration form
        return render(request, 'user_register.html')
def user_settings(request):
    if request.method == 'POST':
        
        pass
    else:
       
        return render(request, 'user_settings.html')
