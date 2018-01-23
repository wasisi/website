from django import forms
from .models import County

class CoffeeGradeForm(forms.Form):
    grade = forms.CharField()
    size = forms.CharField()
    description = forms.TextField()