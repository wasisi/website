# Create your views here.
# views.py
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from common.decorators import ajax_required
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import CoffeeTransactions
from .filters import coffeeAppFilter

from django_tables2 import RequestConfig
from .tables import CoffeeTransactionsTable

from django_filters import rest_framework as filters
from rest_framework import generics

from .serializers import CoffeeTransactionsSerializer

def graph(request):
    return render(request, 'graph/graph.html')

#Prepare data that will be passed into graph.html
def play_count_by_month(request):
    data = CoffeeTransactions.objects.all() \
        .extra(select={'month': connections[CoffeeTransactions.objects.db].ops.date_trunc_sql('month', 'ISODATE')}) \
        .values('month') \
        .annotate(count_items=Count('id'))
    return JsonResponse(list(data), safe=False)


#Detail view for transactions
def transaction_detail(request, id):
       transaction = get_object_or_404(CoffeeTransactions, id=id)
       return render(request,
        'transactions/detail.html',
        {'section': 'transactions',
        'transaction': transaction})

#Use AJAX to like a transaction pg 154
@ajax_required
@login_required
@require_POST
def transaction_like(request):
    transaction_id = request.POST.get('id')
    action = request.POST.get('action')
    if transaction_id and action:
        try:
            transaction = CoffeeTransactions.objects.get(id=transaction_id)
            if action == 'like_transaction':
                transaction.users_like.add(request.user)
            else:
                transaction.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'})

#List view for transactions
@login_required
def transaction_list(request):
    table = CoffeeTransactionsTable(CoffeeTransactions.objects.all())
    RequestConfig(request, paginate={'per_page': 100}).configure(table)
    return render(request, 'transactions/tables2.html', {'table': table})
    
