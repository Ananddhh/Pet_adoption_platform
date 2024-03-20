from django import forms
from .models import Appointment
from .models import ContactSubmission
from django import forms
from .models import AdoptionApplication

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'date', 'time']  
  
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'message']

class AdoptionApplicationForm(forms.ModelForm):
    class Meta:
        model = AdoptionApplication
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email Address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Your Phone Number'}),
            'message': forms.Textarea(attrs={'placeholder': 'Tell us about your interest in adoption'}),
        }