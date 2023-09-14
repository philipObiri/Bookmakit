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
    Validation for the email field that prevents users from registering with an existing
    email address.
    """
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use.')
        return data



"""
Allow users to edit their first name, last name, and email, which are
attributes of the built-in Django User model
"""
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['first_name', 'last_name', 'email']

    
    """
    Validation for the email field that prevents users from changing / updating their 
    existing email address to an existing email address of another user.
    """
    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id)\
                         .filter(email=data)
        if qs.exists():
            raise forms.ValidationError('Email already in use.')
        return data


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