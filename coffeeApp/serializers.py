from rest_framework import serializers
from .models import CoffeeTransactions
import django_filters


class CoffeeTransactionsSerializer(serializers.ModelSerializer):
	class Meta:
		model =  CoffeeTransactions
		fields = ('id','producer','grade', 'buyer',)