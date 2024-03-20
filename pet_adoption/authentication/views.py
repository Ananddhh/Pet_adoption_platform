from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('user_login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserRegistrationForm()
    return render(request, 'user_register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')  #if user.is_staff else 'admin_home'
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'user_login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


def coordinator_home(request):
    # Your view logic here
    return render(request, 'coordinator_home.html')

# def coordinator_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None and user.is_coordinator:
#             login(request, user)
#             return redirect('coordinator_home')  # Redirect to coordinator home page
#         else:
#             # Authentication failed, render login form with error message
#             return render(request, 'coordinator_login.html', {'error': 'Invalid username or password'})
#     else:
#         return render(request, 'coordinator_login.html')

# @login_required
# def coordinator_home(request):
#     if request.user.is_coordinator:
#         return render(request, 'coordinator_home.html')
#     else:
#         # Redirect to login page if the user is not authenticated or not a coordinator
#         return redirect('coordinator_login')

