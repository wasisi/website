from django.conf.urls import url

from . import views

urlpatterns = [
# file upload using import/csv needs work. imports only work from django admin. Error reporting dashboard good in admin
    url(r'^import/dealers/$', views.dealer_upload, name='dealer_upload'), 
]