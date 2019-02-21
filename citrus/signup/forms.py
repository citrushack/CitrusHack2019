from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import AuthenticationForm
# from django.forms.widgets import PasswordInput, TextInput
from .models import MyUser
from .models import Profile

class SignUpForm(UserCreationForm):

   class Meta:
      model = MyUser
      fields = (
         'first_name',
         'last_name',
	 'preferred_name',
         'email', 
         'password1', 
         'password2', 
      )

class ProfileForm(forms.ModelForm):
   #learn or gain textfield is charfield with widget=forms.textarea in modelforms, min_length only in forms
   learn_or_gain = forms.CharField(min_length=250, widget=forms.Textarea)
   # BooleanField default blank is true hence only by setting required=True in forms.py will make it required 
   conduct_box = forms.BooleanField(required=True)
   share_box = forms.BooleanField(required=True)

   class Meta:
      model = Profile
      fields = (
         'school', 
         'level_of_study', 
         'graduation_year',
         'major', 

         'gender',
	 'gender_other', 
         'date_of_birth',
         'race',
	 'race_other',
         'phone_number',
         'shirt_size',
         'dietary_restrictions',

         'linkedin', 
         'github', 
         'additional_link', 
         'description',
         'learn_or_gain',
         'resume',

         'conduct_box',
         'share_box',
      )


# class CustomAuthForm(AuthenticationForm):
#     username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Email'}))
#     password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))
