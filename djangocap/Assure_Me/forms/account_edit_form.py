from django import forms
from Assure_Me.models import User

class AccountEditForm(forms.ModelForm):
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if phone_number != None and phone_number.isdigit() == False:
            raise forms.ValidationError('Field Accepts Numbers Only')
        elif phone_number != None and len(phone_number) != 10:
           raise forms.ValidationError('Must Include an Area Code')

        return phone_number
        
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number')