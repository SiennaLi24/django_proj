from django import forms
from .models import UserProfile, Comment

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['location','qualifications']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['ratePost','comment']
