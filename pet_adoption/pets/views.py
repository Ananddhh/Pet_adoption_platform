from .models import Pet
from .models import LostItem
from .forms import ContactForm
from .models import Appointment
from .forms import AppointmentForm
from django.contrib import messages
from django.http import HttpResponse
from .models import AdoptionApplication
from .forms import AdoptionApplicationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect

def adoption_submit(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the form data to the database
        application = AdoptionApplication(name=name, email=email, message=message)
        application.save()

        # Redirect to a success page or render a success message
        return HttpResponse("Form submitted successfully. Thank you!")
    else:
        # If request method is not POST, render the form page
        return render(request, 'adoption_process.html')

def adoption_process(request):
    if request.method == 'POST':
        form = AdoptionApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Form submitted successfully. Thank you!")
    else:
        form = AdoptionApplicationForm()
    return render(request, 'adoption_process.html', {'form': form})

def lost_found_pets(request):
    # Retrieve all lost items from the database
    lost_items = LostItem.objects.all()
    return render(request, 'lost_found.html', {'lost_items': lost_items})


def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'pet_list.html', {'pets': pets})

def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'pet_detail.html', {'pet': pet})



def event_details(request, event_id):
    # fetch details of a specific event based on event_id
    event = get_object_or_404(Pet, pk=event_id)
    return render(request, 'event_details.html', {'event': event})

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, 'Your appointment has been booked successfully.')
            return redirect('appointment_success')  # Redirect to a success page
        else:
            # Form data is invalid, display form with errors
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AppointmentForm()
    
    return render(request, 'book_appointment.html', {'form': form})



def contact_submit_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            return render(request, 'contact_success.html')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'lost_found.html', {'form': form})