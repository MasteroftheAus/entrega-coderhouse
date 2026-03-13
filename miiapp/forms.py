from django import forms
from .models import post, cathegory, Avatar
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm


class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ["title", "content", "state", "type"]

class UserRegisterForm(UserCreationForm):
  email = forms.EmailField()

  class Meta:
      model = User
      fields = ['username', 'email', 'first_name']

class userForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    email = forms.EmailField()

class CathegoryForm(forms.ModelForm):
    class Meta:
        model = cathegory
        fields = "__all__"

class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(label="Name", required=True)
    last_name = forms.CharField(label="Surname", required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["image"]
