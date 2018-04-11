from django import forms
from django.apps import apps
from basicpagesApp.widgets import WYMEditor

class ArticleAdminModelForm(forms.ModelForm):
	body = forms.CharField(widget=WYMEditor())

	class Meta:
		model = apps.get_model('basicpagesApp', 'Page')
		fields = "__all__"