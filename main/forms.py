from django import forms
from django.forms import ModelForm, Select, Textarea, TextInput, FileInput

from .models import Group, Student, Lecture, Task, Solution


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


class StudentForm(ModelForm):
    """Subscriber Form."""

    group_id = forms.ModelChoiceField(
        queryset=Group.objects.all().order_by('name'),
        empty_label="Оберіть групу",
        widget=forms.Select(
            attrs={"class": "form-control"}
        )
    )

    class Meta:
        """Subscriber Form Meta."""

        model = Student
        fields = ['name', 'surname', 'email', 'group_id']
        widgets = {
            "name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ім'я"
            }
            ),
            "surname": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Прізвище"
            }
            ),
            "email": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Email студента "
            }
            ),
        }

    def save(self, commit=True):
        """Manual save method for Subscriber."""
        print("Subscriber before save")
        # form.ModelForm.save(self,commit)
        stud = super().save(commit=False)
        stud.email = stud.email.title()
        stud.save()
        return stud


class LectureForm(ModelForm):
    """Lecture Form."""

    group_id = forms.ModelChoiceField(
        queryset=Group.objects.all().order_by('name'),
        empty_label="Оберіть групу",
        widget=forms.Select(
            attrs={"class": "form-control"}
        )
    )

    class Meta:
        """Subscriber Form Meta."""

        model = Lecture
        fields = ['title', 'description', 'attachments', 'group_id']
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Тема лекції"
            }
            ),
            "description": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Опис лекції"
            }
            ),
            "attachments": FileInput(attrs={
                "class": "form-control",
                "placeholder": "Матеріали"
            }
            ),
        }


class TaskForm(ModelForm):
    group_id = forms.ModelChoiceField(
        queryset=Group.objects.all().order_by('name'),
        empty_label="Оберіть групу",
        widget=forms.Select(
            attrs={"class": "form-control"}
        )
    )

    class Meta:
        """Subscriber Form Meta."""

        model = Task
        fields = ['title', 'description', 'testfile', 'group_id']
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Назва задачі"
            }
            ),
            "description": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Умова задачі"
            }
            ),
            "testfile": FileInput(attrs={
                "class": "form-control",
                "placeholder": "Тестовий файл"
            }
            ),
        }


class SolutionForm:
    pass