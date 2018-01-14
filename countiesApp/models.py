from django.db import models
from django.conf import settings

# Create your models here.

class County(models.Model):
    county_name = models.CharField(max_length=200, db_index=True)
    county_code = models.CharField(max_length=5, db_index=True)

    def __str__(self):
    	return self.county_name