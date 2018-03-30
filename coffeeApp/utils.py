# coffeeApp/utils.py

from django_tables2 import SingleTableView
from django_tables2.config import RequestConfig

from .tables import CoffeeTransactionsTable
from .models import CoffeeTransactions
from .filters import coffeeAppFilter 

class FilteredTransactionsListView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'

    table_class = CoffeeTransactionsTable
    model = CoffeeTransactions
    template_name = 'transactions/transactionsfilter.html'
    filterset_class = coffeeAppFilter

    def get_queryset(self, **kwargs):
        qs = super(FilteredTransactionsListView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super(FilteredTransactionsListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context