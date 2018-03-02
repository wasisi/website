from django.shortcuts import render
from .apps import MainappConfig

# Import models
from directoryApp.models import Producer, Dealer
from coffeeApp.models import CoffeeTransactions

# Create your views here.

def index(request):
    """
    Renders the view for the main page
    :param request: the request that initiated this action
    :param template: the template that used for the rendering
    """
    num_producers = Producer.objects.count() # The 'all()' is implied by default.
    num_dealers = Dealer.objects.count()
    num_transactions = CoffeeTransactions.objects.count()

    page_data={"page_title":MainappConfig.index_page_name,
                                                          'num_producers':num_producers, 
                                                          'num_dealers':num_dealers, 
                                                          'num_transactions':num_transactions}
    return render(request,MainappConfig.index_page_view_tmpl,page_data)


