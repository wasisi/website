from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import County

class CountyAdmin(admin.ModelAdmin):
	list_display = ['county_name', 'county_code']

admin.site.register(County, CountyAdmin)