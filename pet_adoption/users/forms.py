from django import forms
from django.contrib.auth.models import User

class UserSettingsForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(UserSettingsForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
