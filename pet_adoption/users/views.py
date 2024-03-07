from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages
from .forms import UserSettingsForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserLoginForm, UserRegistrationForm
from pets.models import AdoptionApplication

def admin_profile(request):
    
    adoption_forms = AdoptionApplication.objects.all()
    return render(request, 'admin_profile.html', {'adoption_forms': adoption_forms})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:  
            login(request, user)
            return redirect('admin_profile')  # Redirect to admin profile
        else:
            error_message = "Invalid username or password."
            return render(request, 'admin_login.html', {'error_message': error_message})
    else:
        return render(request, 'admin_login.html')

def update_status(request, form_id, new_status):
    
    form = AdoptionApplication.objects.get(pk=form_id)
    
    form.status = new_status
    form.save()
    
    return redirect('admin_profile')

def admin_logout(request):
    logout(request)
    return redirect('home')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'user_login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('user_login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user_register.html', {'form': form})

    
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
    return render(request, 'profile.html', {'user': user})

def custom_logout(request):
    logout(request)
    return redirect('home')

def home(request):
    # Your view logic here
    return render(request, 'home.html')