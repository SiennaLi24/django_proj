from django import forms
from .models import UserProfile, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['location','qualifications']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['ratePost','comment']

class RegistrationForm(UserCreationForm):

	class Meta:
		model = User
		fields = ("username", "password1", "password2")

	def save(self, commit=True):
		user = super(RegistrationForm, self).save()
		return user
