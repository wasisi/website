from django.db import models

# Add mixins from utilApp
from utilsApp.models import CreationModificationDateMixin
from utilsApp.models import UniqueTitleMixin
from utilsApp.models import ActiveMixin
from utilsApp.models import AffiliationMixin
from utilsApp.models import UniqueIDMixin

# URL resolver needed by the get_absolute_url() 
from django.core.urlresolvers import reverse
# Declare custom manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(active='1')

# Producer model
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

    # Set managers to determine conditions that can be passed to views e.g. show only active
    objects = models.Manager() # The default manager.
    published = PublishedManager() # The Dahl-specific manager.

    # Meta
    class Meta:
        db_table='Producer'
        ordering=('title',)

    def get_absolute_url(self):
        #return reverse('directoryApp:producer_detail', kwargs={'slug': self.slug})
        return reverse('directoryApp:producer_detail', args=[self.id, self.slug])
    def __unicode(self):
        return self.title

# Dealer model
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
    

   