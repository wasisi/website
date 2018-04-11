#coffeeapp/tables.py

import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor

from .models import CoffeeTransactions


class CoffeeTransactionsTable(tables.Table):
    class Meta:
        model = CoffeeTransactions
        template_name = 'django_tables2/bootstrap.html'
        fields = ('isodate', 'saleno', 'producercode', 'buyercode', 'price', 'weight_kgr', 'value', 'grade_gr') # fields to display
        saleno = tables.LinkColumn('transaction_detail', args=[A('pk')])
        empty_text = "There are no transactions matching the search criteria..."
        per_page = 100
