"""wasisi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

from django.conf import settings # needed for file uploads in dev server
from django.conf.urls.static import static # needed for file uploads in dev server. REMOVE for production because of static()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'account/', include('accountApp.urls')),
    url(r'^', include('mainApp.urls', namespace='mainApp')),
    url(r'^', include('contactApp.urls')),
    url(r'^', include('basicpagesApp.urls')),
    url(r'^', include('directoryApp.urls', namespace='directoryApp')),
    url(r'^', include('coffeeApp.urls', namespace='coffeeApp')),
    url(r'^tinymce/', include('tinymce.urls')),   
]

# ONLY for DEVELOPMENT. Do not push to production
if settings.DEBUG:
       urlpatterns += static(settings.MEDIA_URL,
                             document_root=settings.MEDIA_ROOT)