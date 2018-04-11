from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required #for functions
from django.contrib.auth.mixins import LoginRequiredMixin #for class based views
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count # for statistics
from common.decorators import ajax_required
from django.shortcuts import render, get_object_or_404 #render content as list/detail; return errors

# Import resources
from .resources import DealerResource, ProducerResource
# Needed for file import
from tablib import Dataset
# Import models
from .models import Producer, Dealer
from coffeeApp.models import CoffeeTransactions
# Import views
from coffeeApp.views import CoffeeTransactions
# Import tables
from .tables import ProducerTable, DealerTable
from coffeeApp.tables import CoffeeTransactionsTable
# Import utils
from .utils import FilteredProducerListView, FilteredDealerListView, FilteredProducerTransactionsView
# Import filters
from .filters import ProducerFilter, DealerFilter, ProducerTransactionFilter
# Import forms
from .forms import ProducerFormHelper, DealerFormHelper, ProducerTransactionsFormHelper
# Django_tables2
from django_tables2 import SingleTableView

# Create your views here.
def dealer_upload(request):
    if request.method == 'POST':
        dealer_resource = DealerResource()
        dataset = Dataset()
        new_dealers = request.FILES['dealerimport']

        imported_data = dataset.load(new_dealers.read())
        result = dealer_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            dealer_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'importexport/dealerimport.html')

def producer_upload(request):
    if request.method == 'POST':
        producer_resource = ProducerResource()
        dataset = Dataset()
        new_producers = request.FILES['producerimport']

        imported_data = dataset.load(new_producers.read())
        result = producer_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            producer_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'importexport/producerimport.html')    

# Below uses in built DJANGO detail view

class ProducerDetailView(LoginRequiredMixin, UpdateView, FilteredProducerTransactionsView):
    model = Producer
    template_name = 'directory/producer/detail.html'
    fields = '__all__'
    
    # the following lines are not needed to render DetailView and filtered table
    table_class = CoffeeTransactionsTable
    filter_class = ProducerTransactionFilter
    formhelper_class = ProducerTransactionsFormHelper

    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
        context = super(ProducerDetailView, self).get_context_data(**kwargs)
    # Add extra context from another model
        context['table'] = CoffeeTransactionsTable(CoffeeTransactions.objects.filter(producercode__slug__exact=self.kwargs['slug']))
        context['form'] = ProducerTransactionsFormHelper
        return context
    

#def ProducerDetailView(request, id, slug):
    #producer = get_object_or_404(Producer, id=id, slug=slug)
    #producerid = Producer.objects.get(id=id)
    #return render(request, 'directory/producer/detail.html', {'section': 'producers',
     #                                               'producer': producer})     

# we are using custom published manager (published) declared in models.py
# Using the generic ListView offered by Django. This base view is shorter and allows you to list objects of any kind.
# Pagination is passed into the template from pagination.html in template folder.
# Ajax loading approach for producer list view
#class ProducerListView(ListView):
       #queryset = Producer.published.all() # we could also use model = Producer and Django would generate the generic Producer.objects.all() QuerySet for us.
       #context_object_name = 'producers' #we define context
       #paginate_by = 50 # 50 producers in each page
       #template_name = 'directory/list.html'

class ProducerListView(LoginRequiredMixin, FilteredProducerListView):
    model = Producer
    table_class = ProducerTable
    filter_class = ProducerFilter
    formhelper_class = ProducerFormHelper    


def DealerDetailView(request, id, slug):
    dealer = get_object_or_404(Dealer, id=id, slug=slug)
    dealerid = Dealer.objects.get(id=id)
    transactions = CoffeeTransactions.objects.filter(buyercode=dealerid)
    paginator = Paginator(transactions, 8)
    page = request.GET.get('page')
    try:
        transactions = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        transactions = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            # If the request is AJAX and the page is out of range return an empty page
            return HttpResponse('')
        # If page is out of range deliver last page of results
        transactions = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request,
                      'transactions/dealer_table_ajax.html',
                      {'section': 'transactions', 'transactions': transactions})
    return render(request, 'directory/dealer/detail.html', {'section': 'dealer',
                                                    'dealer': dealer,
                                                    'transactions': transactions})    

# we are using custom published manager (published) declared in models.py
# Using the generic ListView offered by Django. This base view is shorter and allows you to list objects of any kind.
# Pagination is passed into the template from pagination.html in template folder.
# class DealerListView(ListView):
       #queryset = Dealer.objects.all() # we could also use model = Producer and Django would generate the generic Producer.objects.all() QuerySet for us.
       #context_object_name = 'dealers' #we define context
       #paginate_by = 50 # 50 producers in each page
       #template_name = 'directory/dealer/list.html'

class DealerListView(LoginRequiredMixin, FilteredProducerListView):
    model = Dealer
    table_class = DealerTable
    filter_class = DealerFilter
    formhelper_class = DealerFormHelper    

