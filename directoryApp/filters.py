# directoryApp.filters.py

# See example in https://github.com/rocket-league-replays/rocket-league-replays/blob/develop/rocket_league/apps/replays/filters.py
# http://django-filter.readthedocs.io/en/latest/guide/usage.html

import django_filters

from django.contrib.auth.models import User
from .models import Producer, Dealer

from coffeeApp.models import CoffeeTransactions
from coffeeApp.views import CoffeeTransactions

class ProducerFilter(django_filters.FilterSet):
    producercode__producer_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Producer
        fields = ['county_name', 'producer_name']
    
class ProducerTransactionFilter(django_filters.FilterSet):
    #producercode__producer_name = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = CoffeeTransactions
        fields = ['id', 'producercode', 'buyercode']


class DealerFilter(django_filters.FilterSet):
    buyercode__title = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Dealer
        fields = ['title']
                