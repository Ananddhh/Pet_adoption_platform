from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import AdoptionApplication, ContactMessage, Appointment
from .forms import AdoptionApplicationForm, CoordinatorProfileForm
from pets.models import AdoptionApplication as PetAdoptionApplication
from pets.models import ContactSubmission as PetContactMessage
#  LostFoundMessage
from .models import CoordinatorProfile
from django.contrib.auth import login, authenticate, logout

# Views for managing adoption applications

@staff_member_required
def manage_adoption_applications(request):
    applications = AdoptionApplication.objects.all()
    return render(request, 'manage_adoption_applications.html', {'applications': applications})

@staff_member_required
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

@staff_member_required
def view_user_messages(request):
    contact_messages = ContactMessage.objects.all()
    return render(request, 'view_user_messages.html', {'contact_messages': contact_messages})

# Views for managing appointments

@staff_member_required
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


def coordinator_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_coordinator:
            login(request, user)
            return redirect('coordinator_home.html')
        else:
            # Authentication failed
            return render(request, 'coordinator\coordinator_login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'coordinator\coordinator_login.html')


def coordinator_home(request):
    if request.user.is_authenticated and request.user.is_coordinator:
        return render(request, 'coordinator_home.html')
    else:
        # unauthorized access
        return redirect('coordinator\coordinator_login')

# profile is not working