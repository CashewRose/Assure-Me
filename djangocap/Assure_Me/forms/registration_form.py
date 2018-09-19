from django import forms
from django.core.exceptions import ValidationError
from Assure_Me.models import User

class RegisterForm(forms.ModelForm):

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if phone_number != None and phone_number.isdigit() == False:
            raise forms.ValidationError('Field Accepts Numbers Only')
        elif phone_number != None and len(phone_number) != 10:
           raise forms.ValidationError('Must Include an Area Code')

        return phone_number
        
    class Meta:
        model = User
        help_texts = {
            'username': None,
        }
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'phone_number')
