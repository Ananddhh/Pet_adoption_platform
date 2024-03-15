# coordinator/forms.py

from django import forms
from .models import AdoptionApplication, CoordinatorProfile

class AdoptionApplicationForm(forms.ModelForm):
    class Meta:
        model = AdoptionApplication
        fields = ['pet_name', 'status']  # Include relevant fields from the AdoptionApplication model

class CoordinatorProfileForm(forms.ModelForm):
    class Meta:
        model = CoordinatorProfile
        fields = ['contact_number', 'responsibilities']  # Include relevant fields from the CoordinatorProfile model
