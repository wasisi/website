from django.db import models
from utilsApp.models import CreationModificationDateMixin
from utilsApp.models import UniqueTitleMixin
from utilsApp.models import ActiveMixin
from utilsApp.models import AffiliationMixin
from utilsApp.models import UniqueIDMixin

class Producer(UniqueIDMixin,UniqueTitleMixin,ActiveMixin,AffiliationMixin,CreationModificationDateMixin):

    """
    Model for producer
    """
    actor = models.CharField(max_length=200)
    ref = models.CharField(max_length=200)

    class Meta:
        db_table='Producer'
        ordering=('title',)

    def __str__(self):
        return self.title

class Dealer(UniqueIDMixin,UniqueTitleMixin,ActiveMixin,AffiliationMixin,CreationModificationDateMixin):
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



# Create your models here.
