from django import forms

SHIFTS = (
    ('1', 'Morning'),
    ('2', 'Afternoon'),
    ('3', 'Evening'),
)

class LogForm(forms.Form):
    first_name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    shift = forms.CharField(max_length=1, widget=forms.Select(choices=SHIFTS, attrs={"class" : "form-control"}), required=True,)
    time_log = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time", "class": "form-control"}))
