from django import forms


SHIFTS = [
    ("morning", "Morning"),
    ("afternoon", "Afternoon"),
    ("evening", "Evening"),
]

class InputForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    shift = forms.ChoiceField(choices=SHIFTS, widget=forms.Select(attrs={"class": "form-control"}))
    time_log = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time", "class": "form-control"}))   