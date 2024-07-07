from django import forms

from .models import Logger

class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'shift': forms.Select(attrs={"class": "form-control"}),
            'time_log': forms.TimeInput(attrs={"type": "time", "class": "form-control"})
        }
