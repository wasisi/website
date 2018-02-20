# Create your views here.
# views.py
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render

from .models import CoffeeTransactions


def graph(request):
    return render(request, 'graph/graph.html')

#Prepare data that will be passed into graph.html
def play_count_by_month(request):
    data = CoffeeTransactions.objects.all() \
        .extra(select={'month': connections[CoffeeTransactions.objects.db].ops.date_trunc_sql('month', 'ISODATE')}) \
        .values('month') \
        .annotate(count_items=Count('id'))
    return JsonResponse(list(data), safe=False)