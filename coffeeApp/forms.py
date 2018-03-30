#coffeeapp/forms.py

from django import forms
from .models import CoffeeGrades, CoffeeTransactions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class CoffeeGradeForm(forms.Form):
    grade = forms.CharField()
    size = forms.CharField()
    description = forms.CharField()

class CoffeeTransactionsFormHelper(FormHelper):
    model = CoffeeTransactions
    form_method = 'GET'
    form_tag = False
    layout = Layout(
        'producercode',
        'buyercode', ButtonHolder(
        Submit('submit',  'Filter', css_class='button white right'),
    ))