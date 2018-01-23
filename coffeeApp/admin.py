# Import admin tools
from django.contrib import admin #We are using ImportExportModelAdmin but admin is needed to register models
from import_export.admin import ImportExportModelAdmin

# Import models
from directoryApp.models import Producer
from directoryApp.models import Dealer
from .models import CoffeeGrades, CoffeeTransactions

# Import resources
from import_export import resources
from coffeeApp.resources import CoffeeTransactionsResource


class CoffeeGradesAdmin(admin.ModelAdmin):
	list_display = ['grade', 'grade_name','size']
	ordering = ['grade']

admin.site.register(CoffeeGrades, CoffeeGradesAdmin)

class CoffeeTransactionsAdmin(ImportExportModelAdmin):
	list_display = ['ISODATE', 'TRANSNR','REF']
	raw_id_fields = ('REF',) #replaces dropdown with search
	ordering = ['ISODATE']
	resource_class = CoffeeTransactionsResource 
	#you need to declare the resource_class or you will get errors like
	#ValueError: invalid literal for int() with base 10: 'Baringo'
	#id, created, updated, title, slug, active, affiliation_name, ref, actor, lat, lon, notes, disambiguation, county_name
	#page 16 of Django by example
	search_fields = ('REF', 'TRANSNR')
	pass

admin.site.register(CoffeeTransactions, CoffeeTransactionsAdmin)

