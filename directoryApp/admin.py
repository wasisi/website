from django.contrib import admin
from . models import Producer
from . models import Dealer



@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
	list_display = ['id','title' ]

@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
	list_display = ['id','title' ]