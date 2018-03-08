from django import forms
from .models import CoffeeGrades

class CoffeeGradeForm(forms.Form):
    grade = forms.CharField()
    size = forms.CharField()
    description = forms.CharField()