# directoryApp/forms.py

from django import forms
from .models import Producer, Dealer
from coffeeApp.models import CoffeeTransactions
from .filters import ProducerTransactionFilter

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Reset

class ProducerFormHelper(FormHelper):
    model = Producer
    form_method = 'GET'
    form_tag = False
    layout = Layout(
        'producer_name',
        'county_name', ButtonHolder(
        Submit('submit',  'Filter', css_class='button white right'),
        Reset('reset', 'reset', css_class='button white right')
    ))

class DealerFormHelper(FormHelper):
    model = Dealer
    form_method = 'GET'
    form_tag = False
    layout = Layout(
        'title', ButtonHolder(
        Submit('submit',  'Filter', css_class='button white right'),
    ))

class ProducerTransactionsFormHelper(FormHelper):
    model = CoffeeTransactions
    form_method = 'GET'
    form_tag = False
    layout = Layout(
        'grade_gr',
        'buyercode', ButtonHolder(
        Submit('submit',  'Filter', css_class='button white right'),
    ))