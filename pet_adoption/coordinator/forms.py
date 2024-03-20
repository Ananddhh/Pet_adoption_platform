from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser  # Import the custom user model
from .models import AdoptionApplication, CoordinatorProfile

class CoordinatorRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email']
        from django import forms

class CoordinatorLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class AdoptionApplicationForm(forms.ModelForm):
    class Meta:
        model = AdoptionApplication
        fields = ['pet_name', 'reason_for_adoption']

class CoordinatorProfileForm(forms.ModelForm):
    class Meta:
        model = CoordinatorProfile
        fields = ['responsibilities', 'contact_number']