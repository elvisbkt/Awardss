from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class UpdateUserForm(forms.ModelForm):
    '''
    Class to enable user to update username and email
    '''
    email = forms.EmailField()
    class Meta:
        model = CustomUser
        fields = ['username','email']

class UpdateProfileForm(forms.ModelForm):
    '''
    Class to enable user to update bio and image
    '''
    class Meta:
        model = Profile
        fields = ['bio','image']