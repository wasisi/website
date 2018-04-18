# directoryApp/templatetags/directoryApp_tags.py

from django import template
register = template.Library()
from coffeeApp.models import CoffeeTransactions
from coffeeApp.views import transaction_list
from directoryApp.views import ProducerTransactionsView

@register.simple_tag

def total_transactions():
	return CoffeeTransactions.objects.count()

@register.inclusion_tag('directory/producer/test.html', takes_context=True)
def transactions(context):
	request = context['request']
	transactionlist = transaction_list(request=request)
	ctx = {'transactionlist': transactionlist}
	return ctx


#def transactions(request, self, **kwargs):
#	filteredtransactions = CoffeeTransactionsTable(CoffeeTransactions.objects.filter(producercode__slug__exact=self.kwargs['slug']))
#	return render(request, 'directory/producer/detail.html', {"filteredtransactions":filteredtransactions})
