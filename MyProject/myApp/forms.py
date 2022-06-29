from dataclasses import fields
from django import forms
from myApp.models import UserProfileInfo
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
  password=forms.CharField(widget=forms.PasswordInput)
  
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['username'].help_text = None
      for x in self.fields:
        print('\n',x,'\n')
  class Meta:
    model=User
    fields=['username','email','password']




class UserProfileForm(forms.ModelForm):
  class Meta:
    model=UserProfileInfo
    fields=['portfolio','profile_image']

