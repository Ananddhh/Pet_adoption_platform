from .models import Pet
from .models import LostItem
from .forms import ContactForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Appointment
from .forms import AppointmentForm
from django.contrib import messages
from django.http import HttpResponse
from .models import AdoptionApplication
from .models import Pet, AdoptionRequest
from .forms import AdoptionApplicationForm
from .models import Pet, LostPet, FoundPet, Appointment, AdoptionRequest, ContactSubmission
from django.shortcuts import render, get_object_or_404,redirect
# from .models import ContactSubmission
from coordinator.decorators import coordinator_required
from django.contrib.auth.decorators import login_required

def contact_submit_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the ContactSubmission model
            contact_submission = form.save(commit=False)  
            contact_submission.save()  

            
            return render(request, 'contact_success.html')  
    else:
        form = ContactForm()
    return render(request, 'lost_found.html', {'form': form})

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Pet, AdoptionRequest

@login_required
def adopt_pet(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)

    if request.method == 'POST':
        existing_request = AdoptionRequest.objects.filter(user=request.user, pet=pet).first()
        if existing_request:
            messages.warning(request, "You have already submitted a request for this pet.")
            return redirect('pet_detail', pk=pet.pk)
        
        try:
            adoption_request = AdoptionRequest.objects.create(user=request.user, pet=pet)
            messages.success(request, f"Your adoption request for {pet.name} has been submitted successfully.")
            return redirect('pet_detail', pk=pet.pk)
        except Exception as e:
            messages.error(request, "Failed to submit adoption request. Please try again later.")
            return redirect('pet_detail', pk=pet.pk)

    return render(request, 'pet_detail.html', {'pet': pet})



def adoption_submit(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        
        application = AdoptionApplication(name=name, email=email, message=message)
        application.save()

        
        return render(request, 'adoption_success.html')
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

def event_details(request, event_id):
    
    return render(request, 'event_details.html')
def event_details1(request, event_id):
    
    return render(request, 'event_details1.html')

def lost_found_pets(request):
   
    lost_items = LostItem.objects.all()
    return render(request, 'lost_found.html', {'lost_items': lost_items})


def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'pet_list.html', {'pets': pets})

def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'pet_detail.html', {'pet': pet})

def pet_list1(request):
    pets = Pet.objects.all()
    return render(request, 'pet_list1.html', {'pets': pets})

@coordinator_required
def pet_detail1(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'pet_detail1.html', {'pet': pet})



def event_details(request, event_id):
    
    event = get_object_or_404(Pet, pk=event_id)
    return render(request, 'event_details.html', {'event': event})

from django.http import HttpResponseRedirect  

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()  # Save the form data to the database
            messages.success(request, 'Your appointment has been booked successfully.')
            print('Form is valid! Redirecting to appointment success page.')  # print statement for debugging
            return HttpResponseRedirect(reverse('appointment_success'))  # HttpResponseRedirect instead of redirect
        else:
            print(form.errors)
            messages.error(request, 'Please correct the errors below.')
            print('Form is not valid! Rendering the same page with errors.')  # print statement for debugging
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

# from django.shortcuts import render
# from .models import Pet, LostPet, FoundPet, Appointment, AdoptionRequest, ContactSubmission

# def all_messages(request):
#     contact_messages = ContactSubmission.objects.all()
#     lost_pets = LostPet.objects.all()
#     found_pets = FoundPet.objects.all()
#     adoption_requests = AdoptionRequest.objects.all()
#     appointments = Appointment.objects.all()
    
#     return render(request, 'all_messages.html', {
#         'contact_messages': contact_messages,
#         'lost_pets': lost_pets,
#         'found_pets': found_pets,
#         'adoption_requests': adoption_requests,
#         'appointments': appointments,
#     })
