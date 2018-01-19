from django.shortcuts import render
from .resources import DealerResource, ProducerResource

# Create your views here.
from tablib import Dataset

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