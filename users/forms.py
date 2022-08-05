from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
    class Meta:
        model = User
        fields = ['username','group','email','password1','password2']