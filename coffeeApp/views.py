#coffeeapp/utils.py

from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required #for functions
from django.contrib.auth.mixins import LoginRequiredMixin #for class based views

from common.decorators import ajax_required
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import CoffeeTransactions
from .filters import coffeeAppFilter
from .tables import CoffeeTransactionsTable
from .utils import FilteredTransactionsListView
from .forms import CoffeeTransactionsFormHelper


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

#Simple list view for transactions with no filter
#@login_required
#def transaction_list(request):
    #table = CoffeeTransactionsTable(CoffeeTransactions.objects.all())
    #RequestConfig(request, paginate={'per_page': 100}).configure(table)
    ## Using RequestConfig automatically pulls values from request.GET and updates the table accordingly.
    ## This enables data ordering and pagination.
    #return render(request, 'transactions/transactionsfilter.html', {'table': table})

#List view for transactions with filter
class transaction_list(LoginRequiredMixin, FilteredTransactionsListView):
    model = CoffeeTransactions
    table_class = CoffeeTransactionsTable
    filter_class = coffeeAppFilter
    formhelper_class = CoffeeTransactionsFormHelper

