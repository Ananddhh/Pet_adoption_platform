from django.shortcuts import render
from .models import Pet

def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'pets/pet_list.html', {'pets': pets})

def pet_detail(request, pk):
    pet = Pet.objects.get(pk=pk)
    return render(request, 'pets/pet_detail.html', {'pet': pet})
