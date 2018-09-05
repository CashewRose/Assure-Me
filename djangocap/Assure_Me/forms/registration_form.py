from django import forms
from Assure_Me.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'phone_number')