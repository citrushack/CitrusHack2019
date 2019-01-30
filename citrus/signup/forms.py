from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from .models import Profile

class SignUpForm(UserCreationForm):
   class Meta:
      model = MyUser
      fields = (
         'first_name',
         'last_name',
         'email', 
         'password1', 
         'password2', 
      )

class ProfileForm(forms.ModelForm):
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
         'date_of_birth',
         'race',
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
