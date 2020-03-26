from django import forms 
from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'birth_date', )


class ChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username','birth_date', )