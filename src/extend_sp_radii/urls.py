"""extend_sp_radii URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.contrib import admin

from add_radii import views as add_radii_views
from add_radii import urls as add_radii_urls
from contact import views as contact_views
from about import views as about_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', add_radii_views.home, name='home'),
    url(r'^about/$', about_views.about, name='about'),
    url(r'^contact/$', contact_views.contact, name='contact'),
    url(r'^(?P<ion_label>.*)/?$', add_radii_views.details, name = 'details'),
    #url(r'^(?P<ion_label>[\w]+)/$', add_radii_views.details, name = 'details'),
#    url(r'^(?P<ion_label2>[\w]+)/$', add_radii_views.details2, name = 'details2'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
