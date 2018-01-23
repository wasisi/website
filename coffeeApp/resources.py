# Import models
from directoryApp.models import Dealer, Producer
from countiesApp.models import County # We are importing a model from another app. This is providing a foreign key
from coffeeApp.models import CoffeeTransactions, CoffeeGrades

# Import resources
from import_export import resources

# Import fields and widgets
from import_export.widgets import ForeignKeyWidget, DateWidget
from import_export.fields import Field

# Define resource for the coffee transactions table
class CoffeeTransactionsResource(resources.ModelResource):
	# class import_export.widgets.ForeignKeyWidget(model, field='pk', *args,**kwawrgs)
	# class import_export.widgets.DateWidget(format=None)
	# model - the model the ForeignKey refers to (required)
	# field - field on the related model used for looking up a particular object
	REF = Field(
		column_name='REF',
		attribute='REF',
		widget=ForeignKeyWidget(model=Producer, field='title'))
	GRADE_GR = Field(
		column_name='GRADE_GR',
		attribute='GRADE_GR',
		widget=ForeignKeyWidget(model=CoffeeGrades, field='grade'))
	BUYERCODE = Field(
		column_name='BUYERCODE',
		attribute='BUYERCODE',
		widget=ForeignKeyWidget(model=Dealer, field='ref'))
	ISODATE = Field(
		column_name='ISODATE',
		attribute='ISODATE',
		widget=DateWidget(format=None)) # You can define format e.g. %Y-%m-%d
	class Meta:
		model = CoffeeTransactions
		#fields = ('county_name',)
		#above can be used to chose fields to be imported
		#id, created, updated, title, slug, active, affiliation_name, ref, actor, lat, lon, notes, disambiguation, county_name
		#Errors
		#ValueError: invalid literal for int() with base 10: 'Baringo' > add resourceclass in admin
		#InvalidDimensions encountered while trying to read file: producerimport.csv >column order has to match the order in ImportExportModelAdmin
		#Duplicate entry 'Chebukaka F.C.S. Ltd' for key 'title' > Title has to be unique
