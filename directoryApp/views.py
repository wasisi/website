from django.shortcuts import render

# Import resources
from .resources import DealerResource, ProducerResource

# Needed for file import
from tablib import Dataset

# Needed to display content as list and return errors
from django.shortcuts import render, get_object_or_404

# Import models
from .models import Producer
from coffeeApp.views import CoffeeTransactions

# Pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Import generic views
from django.views.generic import CreateView, DetailView, ListView
from django.utils import timezone

from django.db.models import Count

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
    #template_name = 'directory/detail.html'
    #model = Producer     

def ProducerDetailView(request, slug):
       producer = get_object_or_404(Producer, slug=slug)
       transactions = CoffeeTransactions.objects.all()[:10]
        
        # List of transactions to be squeezed in here
        

       return render(request, 'directory/detail.html', {'section': 'producer',
                                                        'producer': producer,
                                                        'transactions': transactions})    

# we are using custom published manager (published) declared in models.py
# Using the generic ListView offered by Django. This base view is shorter and allows you to list objects of any kind.
# Pagination is passed into the template from pagination.html in template folder.
class ProducerListView(ListView):
       queryset = Producer.published.all() # we could also use model = Producer and Django would generate the generic Producer.objects.all() QuerySet for us.
       context_object_name = 'producers' #we define context
       paginate_by = 50 # 50 producers in each page
       template_name = 'directory/list.html'


