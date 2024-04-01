from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages
from .forms import UserSettingsForm
from .models import CustomUser, UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserLoginForm, UserRegistrationForm
from pets.models import AdoptionApplication
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from pets.forms import AdoptionApplicationForm, ContactForm, AppointmentForm


@login_required
def submit_adoption_request(request):
    if request.method == 'POST':
        form = AdoptionApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adoption_success')
    else:
        form = AdoptionApplicationForm()
    return render(request, 'adoption_request.html', {'form': form})


@login_required
def submit_contact_message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_message()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# @login_required
# def book_appointment(request):
#     if request.method == 'POST':
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('appointment_success')
#     else:
#         form = AppointmentForm()
#     return render(request, 'book_appointment.html', {'form': form})

def admin_profile(request):
    
    adoption_forms = AdoptionApplication.objects.all()
    return render(request, 'admin_profile.html', {'adoption_forms': adoption_forms})



def update_status(request, form_id, new_status):
    
    form = AdoptionApplication.objects.get(pk=form_id)
    
    form.status = new_status
    form.save()
    
    return redirect('admin_profile')

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'user_login.html', {'form': form})

from .models import CustomUser, UserProfile

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            try:
                user = CustomUser.objects.create_user(username=username, email=email, password=password)
                # Create a UserProfile instance for the registered user
                UserProfile.objects.create(user=user)
                messages.success(request, 'Registration successful. Please log in.')
                return redirect('user_login')
            except IntegrityError:
                messages.error(request, 'Username already exists.')
            except Exception as e:
                messages.error(request, 'An error occurred during registration. Please try again later.')
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

# from .models import UserProfile


from .models import UserProfile

@login_required
def user_profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = None
    return render(request, 'user_profile.html', {'profile': profile})

def logout_view(request):
    logout(request)
 
    return redirect('homepage')

def homepage(request):
    # Your view logic here
    return render(request, 'home.html')