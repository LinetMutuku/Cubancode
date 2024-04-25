from django import forms

from app.models import Guest


class TelPhoneNumberInput(forms.TextInput):
    input_type = 'tel'


class loginform(forms.Form):
    username = forms.CharField(max_length=60, label='username')
    password = forms.CharField(max_length=60, label='password', widget=forms.PasswordInput)


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = '__all__'

        labels = {
            'dob': 'Date of Birth',
            'email': 'Email Address'
        }
        widgets = {
            'phone_number': TelPhoneNumberInput(),
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }
