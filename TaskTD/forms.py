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
