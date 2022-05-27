from django import forms
from .models import UserProfile, Comment, Type
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['location','qualifications', 'image']
        #  widgets = {
        #     'location': TextInput(attrs={
        #         'class': "form-control",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Location'
        #         }),
        #     'qualifcations': Textarea(attrs={
        #         'class': "form-control",
        #         'rows':5,
        #         'cols':20,
        #         }),
        # }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['ratePost','comment']
        #  widgets = {
        #     'ratePost': Select(attrs={
        #         'style': 'max-width: 300px;',
        #
        #         }),
        #     'qualifcations': Textarea(attrs={
        #         'class': "form-control",
        #         'rows':5,
        #         'cols':20,
        #         }),
        # }

class RegistrationForm(UserCreationForm):

	class Meta:
		model = User
		fields = ("username", "password1", "password2")

	def save(self, commit=True):
		user = super(RegistrationForm, self).save()
		return user

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['foodType', 'foodName', 'foodRate', 'foodComment', 'foodImage']
