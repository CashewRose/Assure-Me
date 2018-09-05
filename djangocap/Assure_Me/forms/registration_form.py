from django import forms
from Assure_Me.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        help_texts = {
            'username': None,
        }
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'phone_number')