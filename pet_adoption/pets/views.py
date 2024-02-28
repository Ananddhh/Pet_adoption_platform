from .models import Pet
from .models import LostItem
from .models import Appointment
from .forms import AppointmentForm
from django.http import HttpResponse
from .models import AdoptionApplication
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect

def adoption_submit(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        
        application = AdoptionApplication(name=name, email=email, message=message)
        application.save()

        
        return HttpResponse("Form submitted successfully. Thank you!")
    else:
        
        return render(request, 'adoption_process.html')
def lost_found_pets(request):
    # Retrieve all lost items from the database
    lost_items = LostItem.objects.all()
    return render(request, 'pets/lost_found.html', {'lost_items': lost_items})


def pet_list(request):
    # Retrieve all pets from the database
    pets = Pet.objects.all()
    return render(request, 'pets/pet_list.html', {'pets': pets})

def pet_detail(request, pk):
    # Retrieve specific pet based on  primary key (pk)
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'pets/pet_detail.html', {'pet': pet})

def adoption_process(request):
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


def event_details(request, event_id):
    # fetch details of a specific event based on event_id
    event = get_object_or_404(Pet, pk=event_id)
    return render(request, 'pets/event_details.html', {'event': event})

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('appointment_success')  # Redirect to a success page
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})