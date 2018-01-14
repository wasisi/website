from django.db import models
from utilsApp.models import CreationModificationDateMixin
from utilsApp.models import UniqueTitleMixin


class Page(UniqueTitleMixin,CreationModificationDateMixin):

    """
    Model for basic pages 
    """
    body = models.TextField()


    class Meta:
        db_table='Page'
        ordering=('title',)

    def __str__(self):
        return self.title
