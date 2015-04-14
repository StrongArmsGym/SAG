from django import forms

from .models import SignUp
from .models import UserProfile
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		widgets = {
			'password': forms.PasswordInput(),
		}

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('website', 'picture')
