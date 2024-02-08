
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.forms import UserCreationForm
from .models import Staff



class StaffRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Staff
        fields = ['first_name', 'last_name', 'email', 'department', 'phone_number', 'doctor_type', 'doctor_specialization']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control placeholder-input', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control placeholder-input', 'placeholder': 'Enter Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control placeholder-input', 'placeholder': 'Enter Email'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control placeholder-input', 'placeholder': 'Enter Phone Number'}),
            'doctor_type': forms.TextInput(attrs={'class': 'form-control placeholder-input', 'placeholder': 'Enter Doctor Type'}),
            'doctor_specialization': forms.TextInput(attrs={'class': 'form-control placeholder-input', 'placeholder': 'Enter Doctor Specialization'}),
        }
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields.pop('password1')  # Remove 'password1' field
    #     self.fields.pop('password2')  # Remove 'password2' field
        
    def save(self, commit=True):
        staff = super().save(commit=False)
        staff.set_password('password1')  # Set the password as 'password1' for all users
        staff._state.fields.pop('is_superuser', None)
        if commit:
            staff.save()
        return staff

class StaffLoginForm(AuthenticationForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'] = None  # Remove the username field
        self.fields['email'] = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
  