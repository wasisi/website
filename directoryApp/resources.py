from import_export import resources
from directoryApp.models import Dealer, Producer

# for widgets
from import_export.widgets import ForeignKeyWidget
from import_export.fields import Field

class DealerResource(resources.ModelResource):
	class Meta:
		model = Dealer

# for more options https://django-import-export.readthedocs.io/en/latest/getting_started.html#creating-import-export-resource        

class ProducerResource(resources.ModelResource):
	county_name = Field(
		column_name='county_name',
		attribute='county_name',
		widget=ForeignKeyWidget(model=Producer, field='county_name'))
	class Meta:
		model = Producer
		#fields = ('county_name',)
		#above can be used to chose fields to be imported

#id, created, updated, title, slug, active, affiliation_name, ref, actor, lat, lon, notes, disambiguation, county_name

