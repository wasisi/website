# Import admin tools
from django.contrib import admin #We are using ImportExportModelAdmin but admin is needed to register models
from import_export.admin import ImportExportModelAdmin

# Import models
from directoryApp.models import Producer
from directoryApp.models import Dealer

# Import resources
from import_export import resources
from directoryApp.resources import ProducerResource

@admin.register(Producer)
class ProducerAdmin(ImportExportModelAdmin): #replace admin.ModelAdmin with ImportExportModelAdmin
	list_display = ['producer_name','title', 'county_name' ]
	resource_class = ProducerResource 
	#you need to declare the resource_class or you will get errors like
	#ValueError: invalid literal for int() with base 10: 'Baringo'
	#id, created, updated, title, slug, active, affiliation_name, ref, actor, lat, lon, notes, disambiguation, county_name
	#page 16 of Django by example
	list_filter = ('actor', 'created', 'updated', 'county_name')
	search_fields = ('title', 'producer_name')
	prepopulated_fields = {'slug': ('producer_name',)}
	ordering = ['producer_name','title','county_name']

@admin.register(Dealer)
class DealerAdmin(ImportExportModelAdmin): #replace admin.ModelAdmin with ImportExportModelAdmin
	list_display = ['ref','title', 'website' ]
	pass
