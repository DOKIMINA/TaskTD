from django import forms
from .models import Task, Coment

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed_at', 'status',
                      'prior', 'deadline', 'workers', 'attachment']

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введіть назву завдання",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Опис завдання...",
            }),
            "completed_at": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                },
                format="%Y-%m-%dT%H:%M",
            ),
            "status": forms.Select(attrs={
                "class": "form-select",
            }),
            "prior": forms.Select(attrs={
                "class": "form-select",
            }),
            "deadline": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                },
                format="%Y-%m-%dT%H:%M",
            ),
            "workers": forms.SelectMultiple(attrs={
                "class": "form-select",
                "size": "4",
            }),
            "attachment": forms.ClearableFileInput(attrs={
                "class": "form-control",
            }),
        }

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control form-control-sm border-0 bg-light p-2 rounded-2'
            })


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control form-control-sm border-0 bg-light p-2 rounded-2'
            })