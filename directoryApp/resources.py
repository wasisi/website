# Import models
from directoryApp.models import Dealer, Producer
from countiesApp.models import County # We are importing a model from another app. This is providing a foreign key

# Import resources
from import_export import resources

# Import fields and widgets
from import_export.widgets import ForeignKeyWidget
from import_export.fields import Field

# Define resource for the Dealer table
class DealerResource(resources.ModelResource):
	class Meta:
		model = Dealer
		# for more options 
		# https://django-import-export.readthedocs.io/en/latest/getting_started.html#creating-import-export-resource        

# Define resource for the producer table
class ProducerResource(resources.ModelResource):
	# class import_export.widgets.ForeignKeyWidget(model, field='pk', *args,**kwawrgs)
	# model - the model the ForeignKey refers to (required)
	# field - field on the related model used for looking up a particular object
	county_name = Field(
		column_name='county_name',
		attribute='county_name',
		widget=ForeignKeyWidget(model=County, field='county_name'))
	class Meta:
		model = Producer
		#fields = ('county_name',)
		#above can be used to chose fields to be imported
		#id, created, updated, title, slug, active, affiliation_name, ref, actor, lat, lon, notes, disambiguation, county_name
		#Errors
		#ValueError: invalid literal for int() with base 10: 'Baringo' > add resourceclass in admin
		#InvalidDimensions encountered while trying to read file: producerimport.csv >column order has to match the order in ImportExportModelAdmin
		#Duplicate entry 'Chebukaka F.C.S. Ltd' for key 'title' > Title has to be unique



