from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField( required=False )
    class Meta:
        model= User
        fields = ["username" , 'email', 'password1', 'password2']
        
        # this doesnot work for password field that why i commented it out in replace use init method
        # widgets = {
        #     'username': forms.TextInput(attrs={'placeholder': 'Username'}),
        #     'password1': forms.PasswordInput(
        #         attrs={'placeholder': 'Enter password'}),
        #     'password2': forms.PasswordInput(attrs={"placeholder": 'confirm password'})
        # }
        
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'email@address.nl'
        self.fields['password1'].widget.attrs['placeholder'] = 'Create password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        
        