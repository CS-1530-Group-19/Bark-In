"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from django.forms import ModelForm
from app.models import UserProfile,Dog,ParkReview,Schedule
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class EditProfileForm(ModelForm):
    bio = forms.CharField(max_length=256)
    password = forms.PasswordInput({'class': 'form-control','placeholder':'Password'})
    class Meta:
        model=User
        fields = ('password','bio')

class SignUpForm(UserCreationForm):
    bio = forms.CharField(max_length=256)

    class Meta:
        model = User
        fields = ('username','bio')

class AddDogForm(ModelForm):
    name = forms.CharField(max_length = 150)
    dog_pfp = forms.FileField(label = 'select a picture')
    class Meta:
        model = Dog
        fields = ('name','breed','dog_size','temperament','activity_level','volume','notes','dog_pfp')

class AddReviewForm(ModelForm):
    class Meta:
        model = ParkReview
        fields = ('star_rating','review')

class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ('date','t_start', 't_end')

class EditDogForm(ModelForm):
    dog_pfp = forms.FileField(label = 'select a picture')
    class Meta:
        model = Dog
        fields = ('name','breed','dog_size','temperament','activity_level','volume','notes','dog_pfp')
