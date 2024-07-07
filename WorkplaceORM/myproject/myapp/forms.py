from django import forms

from django.forms.widgets import NumberInput

FAVOURITE_DISH = [
    ('italian', 'Italian'),
    ('greek', 'Greek'),
    ('turkish', 'Turkish'),
]

class DemoForm(forms.Form):
    reservation_date = forms.DateField(widget=NumberInput(attrs={"type": "date", "class": "form-control"}))
    favorite_dish = forms.ChoiceField(choices=FAVOURITE_DISH, widget=forms.RadioSelect(attrs={"class": "form-control"}))