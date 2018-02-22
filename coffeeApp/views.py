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
    transactions = CoffeeTransactions.objects.all()
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
                      'transactions/list_ajax.html',
                      {'section': 'transactions', 'transactions': transactions})
    return render(request,
                  'transactions/list.html',
                   {'section': 'transactions', 'transactions': transactions})

#List view for producer transactions
@login_required
def producer_transaction_list(request):
    producer_transactions = CoffeeTransactions.objects.all()
    paginator = Paginator(producer_transactions, 8)
    page = request.GET.get('page')
    try:
        producer_transactions = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        producer_transactions = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            # If the request is AJAX and the page is out of range return an empty page
            return HttpResponse('')
        # If page is out of range deliver last page of results
        producer_transactions = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request,
                      'transactions/producer_list_ajax.html',
                      {'section': 'producer_transactions', 'producer_transactions': producer_transactions})
    return render(request,
        'transactions/list.html',
        {'section': 'producer_transactions', 'producer_transactions': producer_transactions}) 

