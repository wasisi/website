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
    #Temporary approach for searching for counties. Look up table to be done
    COUNTY_CHOICES = (
    ('1', '_Unknown'),
    ('2', 'Baringo'),
    ('3', 'Bungoma'),
    ('4', 'Busia'),
    ('5', 'Embu'),
    ('6', 'Kakamega'),
    ('7', 'Kericho'),
    ('8', 'Kiambu'),
    ('9', 'Kirinyaga'),
    ('10', 'Kisii'),
    ('11', 'Machakos'),
    ('12', 'Makueni'),
    ('13', 'Meru'),
    ('14', 'Migori'),
    ('15', 'Muranga'),
    ('16', 'Nakuru'),
    ('17', 'Nandi'),
    ('18', 'Nyamira'),
    ('19', 'Nyeri'),
    ('20', 'Siaya'),
    ('21', 'YT'),
    ('22', 'Makueni'),
    ('23', 'YT'),
    ('24', 'Baringo'),
    ('25', 'Bungoma'),
    ('26', 'Busia'),
    ('27', 'Embu'),
    ('28', 'Kakamega'),
    ('29', 'Kericho'),
    ('30', 'Kiambu'),
    ('31', 'Kirinyaga'),
    ('32', 'Kisii'),
    ('33', 'Machakos'),
    ('34', 'Makueni'),
    ('35', 'Meru'),
    ('36', 'Migori'),
    ('37', 'Muranga'),
    ('38', 'Nakuru'),
    ('39', 'Nandi'),
    ('40', 'Nyamira'),
    ('41', 'Nyeri'),
    ('42', 'Siaya'),
    ('43', 'YT'),
    ('44', 'Makueni'),
    ('45', 'YT'),
    ('46', 'YT'),
    ('47', 'Makueni'),
)
    ref = models.CharField(max_length=200)
    actor = models.CharField(max_length=20,
    						choices=PRODUCER_CHOICES,
    						default='estate_small')
    lat = models.FloatField(default=0.0, blank=True, null=True)
    lon = models.FloatField(default=0.0, blank=True, null=True)
    notes = models.CharField(max_length=200, null=True, blank=True)
    county = models.CharField(max_length=200, 
    						 choices=COUNTY_CHOICES, 
    						 null=True, 
    						 blank=True)
    #county = models.ForeignKey(county, null=True,blank=True, related_name="county_name")
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
    ref = models.CharField(max_length=200)
    active_website =models.BooleanField(default=True)

    class Meta:
        db_table='Dealer'
        ordering=('title',)

    def __str__(self):
        return self.title