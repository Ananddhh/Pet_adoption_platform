from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'date', 'time']  # Assuming these are the fields in our Appointment model


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

from django import forms
from .models import AdoptionApplication

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