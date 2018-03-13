# See example in https://github.com/rocket-league-replays/rocket-league-replays/blob/develop/rocket_league/apps/replays/filters.py
# http://django-filter.readthedocs.io/en/latest/guide/usage.html

#from django_filters import rest_framework as filters # ImportError: cannot import name 'rest_framework'
import django_filters
#import rest_framework as filters  # AttributeError: module 'rest_framework' has no attribute 'FilterSet'
#import rest_framework_filters as filters


from django.contrib.auth.models import User
from .models import CoffeeTransactions, CoffeeGrades

#class coffeeAppFilter(filters.FilterSet):
class coffeeAppFilter(django_filters.FilterSet):
    # producercode__producer_name = django_filters.CharFilter(lookup_expr='icontains')
    # buyercode__title = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = CoffeeTransactions
        fields = ['producercode', 'buyercode']    