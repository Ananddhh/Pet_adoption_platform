from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CoordinatorRegistrationForm,CoordinatorLoginForm
from .models import Coordinator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import AdoptionApplication, ContactMessage, Appointment, CoordinatorProfile
from .forms import  CoordinatorRegistrationForm, CoordinatorLoginForm,AdoptionApplicationForm, CoordinatorProfileForm
from pets.models import AdoptionApplication as PetAdoptionApplication
from pets.models import ContactSubmission as PetContactMessage

def coordinator_register(request):
    if request.method == 'POST':
        form = CoordinatorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Additional coordinator-specific data
            Coordinator.objects.create(user=user)
            return redirect('coordinator_login')
    else:
        form = CoordinatorRegistrationForm()
    return render(request, 'coordinator_register.html', {'form': form})

def coordinator_login(request):
    if request.method == 'POST':
        # Handle POST request for logging in
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to coordinator dashboard or desired page
            return redirect('coordinator_dashboard')
        else:
            # Handle invalid login
            return render(request, 'coordinator_login.html', {'error': 'Invalid credentials'})
    else:
        # Handle GET request for displaying login form
        form = CoordinatorLoginForm()  # Assuming you have a form for login
        return render(request, 'coordinator_login.html', {'form': form})

def coordinator_dashboard(request):
    
    return render(request, 'coordinator_home.html')

def manage_adoption_applications(request):
    applications = AdoptionApplication.objects.all()
    return render(request, 'manage_adoption_applications.html', {'applications': applications})

def update_request_status(request, application_id):
    application = get_object_or_404(AdoptionApplication, id=application_id)
    if request.method == 'POST':
        form = AdoptionApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('manage_adoption_applications')
    else:
        form = AdoptionApplicationForm(instance=application)
    return render(request, 'update_request_status.html', {'form': form, 'application': application})

# Views for managing user messages
def view_user_messages(request):
    contact_messages = ContactMessage.objects.all()
    return render(request, 'view_user_messages.html', {'contact_messages': contact_messages})

# Views for managing appointments
def manage_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'manage_appointments.html', {'appointments': appointments})

# Coordinator profile views
@login_required
def coordinator_profile(request):
    profile = CoordinatorProfile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})

@login_required
def update_coordinator_profile(request):
    profile = CoordinatorProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = CoordinatorProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('coordinator_profile')
    else:
        form = CoordinatorProfileForm(instance=profile)
    return render(request, 'update_profile.html', {'form': form})