from .models import Pet
from .models import LostItem
from .forms import ContactForm
from .models import Appointment
from .forms import AppointmentForm
from django.contrib import messages
from django.http import HttpResponse
from .models import AdoptionApplication
from .models import Pet, AdoptionRequest
from .forms import AdoptionApplicationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from .models import ContactSubmission  # Import the ContactSubmission model

def contact_submit_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the ContactSubmission model
            contact_submission = form.save(commit=False)  # Create an instance of ContactSubmission model
            contact_submission.save()  # Save the instance to the database

            # Optionally, you can display a success message or redirect to a success page
            return render(request, 'contact_success.html')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'lost_found.html', {'form': form})


def adopt_pet(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    
    
    user = request.user
    
    
    existing_request = AdoptionRequest.objects.filter(user=user, pet=pet).first()
    if existing_request:
    
        messages.warning(request, "You have already submitted a request for this pet.")
        return redirect('pet_detail', pet_id=pet.id)
    
    
    adoption_request = AdoptionRequest.objects.create(user=user, pet=pet)
    
    
    admin_email = 'admin@example.com'  # admin email
    subject = f"New Adoption Request for {pet.name}"
    message = f"User {user.username} has submitted an adoption request for {pet.name}."
    
    messages.success(request, f"Your adoption request for {pet.name} has been submitted successfully.")
    
    
    return redirect('pet_detail', pet_id=pet.id)

def adoption_submit(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        
        application = AdoptionApplication(name=name, email=email, message=message)
        application.save()

        
        return HttpResponse("Form submitted successfully. Thank you!")
    else:
       
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
            print('appointment booked success')

            return redirect('appointment_success')  # Redirect to a success page
        else:
            # Form data is invalid, display form with errors
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AppointmentForm()
    
    return render(request, 'book_appointment.html', {'form': form})

def appointment_success(request):
    return render(request, 'appointment_success.html')

# def contact_submit_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
            
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
            
#             return render(request, 'contact_success.html')  # Redirect to a success page
#     else:
#         form = ContactForm()
#     return render(request, 'lost_found.html', {'form': form})