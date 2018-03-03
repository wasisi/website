from django.conf.urls import url

from . import views

# from models import Task

urlpatterns = [
# file upload using import/csv needs work. imports only work from django admin. Error reporting dashboard good in admin
    url(r'^import/dealers/$', views.dealer_upload, name='dealer_upload'),
    #url(r'^directory/producers$', views.producer_list, name='producer_list'), #replaced with class based view below
    url(r'^directory/producers$', views.ProducerListView.as_view(), name='producer_list'),
    url(r'^producer/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProducerDetailView, name='producer_detail'),
    url(r'^directory/dealers$', views.DealerListView.as_view(), name='dealer_list'),
    url(r'^dealer/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.DealerDetailView, name='dealer_detail'),
]