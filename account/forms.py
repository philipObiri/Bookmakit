from django import forms
from django.contrib.auth.models import User
from .models import Profile 

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget= forms.PasswordInput)


# Registration
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
    widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
    widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    """
    compare the second password against the first one
    and raise a validation error if the passwords don’t match 
    """
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']



"""
Allow users to edit their first name, last name, and email, which are
attributes of the built-in Django User model
"""
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['first_name', 'last_name', 'email']


"""
Allow users to edit the profile data that is saved in the Custom
Profile model extending the built in User Model. 
Users will be able to edit their date of birth and upload an image for their
profile picture.
"""
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']