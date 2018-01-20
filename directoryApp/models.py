from django.db import models
from utilsApp.models import CreationModificationDateMixin
from utilsApp.models import UniqueTitleMixin
from utilsApp.models import ActiveMixin
from utilsApp.models import AffiliationMixin
from utilsApp.models import UniqueIDMixin

class Producer(UniqueTitleMixin,ActiveMixin,AffiliationMixin,CreationModificationDateMixin):

    """
    Model for producer
    """
    PRODUCER_CHOICES = ( 
    	('coop', 'Cooperative Society'),
    	('estate_large', 'Estate Producers'),
    	('estate_small', 'Small estates'),
    	('factory','Factory'),
    	)
    
    producer_name = models.CharField(max_length=200) # can't be unique because there are producers that share the same names
    actor = models.CharField(max_length=20,
    						choices=PRODUCER_CHOICES,
    						default='estate_small')
    lat = models.FloatField(default=0.0, blank=True, null=True)
    lon = models.FloatField(default=0.0, blank=True, null=True)
    notes = models.CharField(max_length=200, null=True, blank=True)
    disambiguation = models.CharField(max_length=200, null=True, blank=True)
    
    # Lazy referencing to model contained in another app
    county_name = models.ForeignKey('countiesApp.County')

    class Meta:
        db_table='Producer'
        ordering=('title',)

    def __str__(self):
        return self.title

class Dealer(UniqueTitleMixin,ActiveMixin,AffiliationMixin,CreationModificationDateMixin):
    """
    Model for dealer
    """
    
    website = models.CharField(max_length=200)
    ref = models.CharField(max_length=200, unique=True)
    active_website =models.BooleanField(default=True)

    class Meta:
        db_table='Dealer'
        ordering=('title',)

    def __str__(self):
        return self.title