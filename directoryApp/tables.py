#directoryapp/tables.py

import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor

from .models import Producer, Dealer
from . import views



class ProducerTable(tables.Table):
    producer_name = tables.TemplateColumn('<a href="{{record.get_absolute_url}}">{{record.producer_name}}</a>')

    class Meta:
        model = Producer
        template_name = 'django_tables2/bootstrap.html'
        fields = ('producer_name', 'title', 'actor', 'county_name', 'disambiguation') # fields to display
        #saleno = tables.LinkColumn('transaction_detail', args=[A('pk')])
        empty_text = "There are no results matching the search criteria..."
        per_page = 100

class DealerTable(tables.Table):
    title = tables.TemplateColumn('<a href="{{record.get_absolute_url}}">{{record.title}}</a>')
    
    class Meta:
        model = Dealer
        template_name = 'django_tables2/bootstrap.html'
        fields = ('title', 'ref', 'website') # fields to display
        empty_text = "There are no results matching the search criteria..."
        per_page = 100