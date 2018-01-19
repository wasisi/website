from import_export.admin import ImportExportModelAdmin

from import_export import resources



from django.contrib import admin
from directoryApp.models import Producer
from directoryApp.models import Dealer

# for widgets
from import_export.widgets import ForeignKeyWidget
from import_export.fields import Field

from directoryApp.resources import ProducerResource


@admin.register(Producer)
class ProducerAdmin(ImportExportModelAdmin): #replace admin.ModelAdmin with ImportExportModelAdmin
	list_display = ['ref','title', 'county_name' ]
	#resource_class = ProducerResource 
	#you need to declare the resource_class but when I get problems.
	#ValueError: invalid literal for int() with base 10: 'Baringo'

@admin.register(Dealer)
class DealerAdmin(ImportExportModelAdmin): #replace admin.ModelAdmin with ImportExportModelAdmin
	list_display = ['ref','title', 'website' ]
	pass
