from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^login/$',
			views.log_in,
			name='log_in'),

    url(r'^profile/$',
			  views.user_profile,
			  name='user_profile'),
 ]