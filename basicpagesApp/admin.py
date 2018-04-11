from django.contrib import admin
from . models import Page
from django.apps import apps
from basicpagesApp.forms import ArticleAdminModelForm


#@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
	list_display = ['id','title' ]
	form = ArticleAdminModelForm
    
admin.site.register(apps.get_model('basicpagesApp', 'Page'), PageAdmin)
