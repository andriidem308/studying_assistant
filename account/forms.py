from account.models import User
from django import forms
from django.utils.text import slugify


class UserRegisterForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    confirmation_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'confirmation_password')

    def clean(self):
        clean_data: dict = super().clean()
        if clean_data['password'] != clean_data['confirmation_password']:
            self.add_error('password', 'Password mismatch!')


        if not clean_data['username']:
            clean_data['username'] = slugify(clean_data['first_name'])
        return clean_data

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=email).exists():
            self.add_error('email', 'Email already exists!')
        return email

