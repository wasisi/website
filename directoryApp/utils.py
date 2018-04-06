# directoryApp/utils.py

from django_tables2 import SingleTableView
from django.views.generic import TemplateView
from django_tables2.config import RequestConfig
from django.shortcuts import render, get_object_or_404

from .tables import ProducerTable, DealerTable
from .models import Producer, Dealer
from .filters import ProducerFilter, DealerFilter, ProducerTransactionFilter

from coffeeApp.models import CoffeeTransactions
from coffeeApp.filters import coffeeAppFilter
from coffeeApp.tables import CoffeeTransactionsTable

class FilteredProducerListView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'

    table_class = ProducerTable
    model = Producer
    template_name = 'directory/producer/list.html'
    filterset_class = ProducerFilter

    def get_queryset(self, **kwargs):
        qs = super(FilteredProducerListView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super(FilteredProducerListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context


class FilteredProducerTransactionsView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'

    table_class = CoffeeTransactionsTable
    model = CoffeeTransactions
    template_name = 'directory/producer/detail.html'
    filterset_class = ProducerTransactionFilter

    def get_queryset(self, **kwargs):
        qs = super(FilteredProducerTransactionsView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super(FilteredProducerTransactionsView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context        
        

class FilteredDealerListView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'

    table_class = DealerTable
    model = Producer
    template_name = 'directory/dealer/list.html'
    filterset_class = DealerFilter

    def get_queryset(self, **kwargs):
        qs = super(FilteredDealerListView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super(FilteredDealerListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context
