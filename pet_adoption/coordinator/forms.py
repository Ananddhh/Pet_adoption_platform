from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser  # Import the custom user model
from .models import BookingAppointment, AdoptionRequest, ContactSubmission,CoordinatorProfile
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CoordinatorRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class CoordinatorLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


from django import forms
from .models import BookingAppointment, AdoptionRequest, ContactSubmission

class BookingAppointmentForm(forms.ModelForm):
    class Meta:
        model = BookingAppointment
        fields = ['name', 'email', 'date', 'time']

class AdoptionRequestForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequest
        fields = ['user', 'pet', 'status']

class ContactSubmissionForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'message']

class CoordinatorProfileForm(forms.ModelForm):
    class Meta:
        model = CoordinatorProfile
        fields = ['responsibilities', 'contact_number']