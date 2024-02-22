from django.shortcuts import render
from .models import Pet

def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'pets/pet_list.html', {'pets': pets})

def pet_detail(request, pk):
    pet = Pet.objects.get(pk=pk)
    return render(request, 'pets/pet_detail.html', {'pet': pet})
def adoption_process(request):
    # Logic for the adoption process view
    return render(request, 'adoption.html')

def event_details(request, event_id):
    # Logic to fetch details of a specific event based on event_id
    try:
        event = Pet.objects.get(pk=event_id)
    except Pet.DoesNotExist:
        event = None
    return render(request, 'event_details.html', {'event': event})

