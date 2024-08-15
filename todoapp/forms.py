from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model() 

class TodoForm(forms.Form):
    text = forms.CharField(
        max_length=100,
        required=True,
        error_messages={
            'required': 'This field is required.',
            'max_length': 'Text cannot be longer than 300 characters.',
        },
        widget=forms.TextInput(attrs={'placeholder': 'Enter your todo'})
    )


class UserRegistrationForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        error_messages={
            'required': 'Name is required.',
            'max_length': 'Name cannot exceed 100 characters.',
        },
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'})
    )
    email = forms.EmailField(
        required=True,
        error_messages={
            'required': 'Email is required.',
            'invalid': 'Enter a valid email address.',
        },
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        error_messages={
            'required': 'Password is required.',
        }
    )
    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}),
        error_messages={
            'required': 'Please confirm your password.',
        }
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email is already taken')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError('Passwords do not match')

        return cleaned_data
    

class UserLoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        error_messages={
            'required': 'Email is required.',
            'invalid': 'Enter a valid email address.',
        }
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        error_messages={
            'required': 'Password is required.',
        }
    )
