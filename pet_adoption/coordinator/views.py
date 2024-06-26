from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CoordinatorRegistrationForm, CoordinatorLoginForm, CoordinatorProfileForm
from .models import Coordinator, CoordinatorProfile
from pets.forms import AdoptionApplicationForm  
from pets.models import AdoptionApplication, Appointment
from pets.models import ContactSubmission as ContactMessage
from django.shortcuts import render
from .models import ContactSubmission
from pets.models import FoundPet
from coordinator.models import  BookingAppointment
# from .views import all_messages
from django.shortcuts import render
from pets.models import LostPet, FoundPet, Appointment, AdoptionRequest, ContactSubmission
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Coordinator
from .models import CoordinatorProfile
from pets.models import AdoptionRequest
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
# from .models import CoordinatorProfile
from pets.models import AdoptionApplication
# coordinator/views.py
from .models import Coordinator
from .decorators import coordinator_required


@coordinator_required
def coordinator_profile(request):
    try:
        coordinator = Coordinator.objects.get(user=request.user)
        
    except Coordinator.DoesNotExist:
        coordinator = None
        
    return render(request, 'coordinator_profile.html', {'coordinator': coordinator})


@coordinator_required
def adoption_requests(request):
    try:
        coordinator = Coordinator.objects.get(user=request.user)
        adoption_requests = AdoptionApplication.objects.all()
    except Coordinator.DoesNotExist:
        coordinator = None
        adoption_requests = None
        
    return render(request, 'adoption_req.html', {'coordinator': coordinator, 'adoption_requests': adoption_requests})

@coordinator_required
def all_messages(request):
    contact_messages = ContactSubmission.objects.all()
    lost_pets = LostPet.objects.all()
    found_pets = FoundPet.objects.all()
    adoption_requests = AdoptionApplication.objects.all()
    # appointments = Appointment.objects.all()
    
    return render(request, 'all_messages.html', {
        'contact_messages': contact_messages,
        'lost_pets': lost_pets,
        'found_pets': found_pets,
        # 'adoption_requests': adoption_requests,
    })


def coordinator_register(request):
    if request.method == 'POST':
        form = CoordinatorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            Coordinator.objects.create(user=user)
            return redirect('coordinator_login')
    else:
        form = CoordinatorRegistrationForm()
    return render(request, 'coordinator_register.html', {'form': form})

def coordinator_login(request):
    if request.method == 'POST':
        
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            return redirect('coordinator_dashboard')
        else:
            # Handle invalid login
            return render(request, 'coordinator_login.html', {'error': 'Invalid credentials'})
    else:
        
        form = CoordinatorLoginForm()  
        return render(request, 'coordinator_login.html', {'form': form})
    
@coordinator_required
def coordinator_dashboard(request):
    
    return render(request, 'coordinator_home.html')

@coordinator_required
def manage_adoption_applications(request):
    applications = AdoptionRequest.objects.all()
    return render(request, 'manage_adoption_applications.html', {'applications': applications})

@coordinator_required
def update_request_status(request, application_id):
    application = get_object_or_404(AdoptionApplication, id=application_id)
    if request.method == 'POST':
       
        form = AdoptionApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('manage_adoption_applications')
    else:
        from .forms import AdoptionApplicationForm
        form = AdoptionApplicationForm(instance=application)
    return render(request, 'update_request_status.html', {'form': form, 'application': application})


@coordinator_required
def view_user_messages(request):
    contact_messages = ContactMessage.objects.all()
    return render(request, 'view_user_messages.html', {'contact_messages': contact_messages})

@coordinator_required
def manage_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'manage_appointments.html', {'appointments': appointments})


# @login_required
# def coordinator_profile(request):
#     # Get the coordinator profile for the currently logged-in user
#     coordinator_profile = get_object_or_404(Coordinator, user=request.user)
#     return render(request, 'coordinator_profile.html', {'coordinator_profile': coordinator_profile})
@coordinator_required
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

def coordinator_logout(request):
    logout(request)
    return redirect('coordinator_login') 

from django.contrib.auth.models import User  

def set_coordinator_credentials(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        coordinator = Coordinator.objects.first()  
        if coordinator:
            user = coordinator.user
            user.username = username
            user.set_password(password)
            user.save()
        else:
            
            user = User.objects.create_user(username=username, password=password)
            Coordinator.objects.create(user=user)
        return redirect('coordinator_login')
    else:
        return render(request, 'set_coordinator_credentials.html')