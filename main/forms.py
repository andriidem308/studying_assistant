from django import forms
from django.forms import ModelForm, Select, Textarea, TextInput

from .models import Group, Student, Material


class GroupForm(ModelForm):
    """Group Form."""

    class Meta:
        """Form Meta."""

        model = Group
        fields = ['name']
        widgets = {
            "name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Назва групи"
            }),
        }
