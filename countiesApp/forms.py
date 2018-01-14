from django import forms
from .models import County

class CountyForm(forms.Form):
    county_name = forms.CharField()
    county_code = forms.CharField()