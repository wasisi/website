from django.shortcuts import render

# Import resources
from .resources import DealerResource, ProducerResource

# Needed for file import
from tablib import Dataset

# Needed to display content as list and return errors
from django.shortcuts import render, get_object_or_404

# Import dependencies
from .models import Producer, Dealer
from coffeeApp.views import CoffeeTransactions

from .filters import ProducerFilter, DealerFilter, ProducerTransactionFilter
from .tables import ProducerTable, DealerTable
from .utils import FilteredProducerListView, FilteredDealerListView, FilteredProducerTransactionsView
from .forms import ProducerFormHelper, DealerFormHelper

from coffeeApp.tables import CoffeeTransactionsTable
from coffeeApp.forms import CoffeeTransactionsFormHelper

# Pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Import generic views
from django.views.generic import CreateView, DetailView, ListView
from django.utils import timezone

from django.db.models import Count
from django.http import HttpResponse
from common.decorators import ajax_required
from django.contrib.auth.decorators import login_required #for functions
from django.contrib.auth.mixins import LoginRequiredMixin #for class based views
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
#class ProducerDetailView(DetailView):
 #   template_name = 'directory/producer/detail.html'
  #  model = Producer  


class ProducerTransactionsView(LoginRequiredMixin, FilteredProducerTransactionsView): 
    model = CoffeeTransactions
    table_class = CoffeeTransactionsTable
    filter_class = ProducerTransactionFilter
    formhelper_class = CoffeeTransactionsFormHelper 

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

