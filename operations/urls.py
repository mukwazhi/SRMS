
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from  django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^report_list/$', views.report_list, name='report_list'),
    url(r'^assessmentList/$', views.assessmentList, name='assessmentList'),
    # url(r'^assessmentList/(?P<report_no>[\w-]+)/$', views.assessmentList, name='assessmentList'),
    url(r'^riskform/$', views.riskform, name='riskform'),
    url(r'^searchHazard/$', views.searchHazard, name='searchHazard'),
    url(r'^quickView/$', views.quickView, name='quickView'),
    url(r'^openhazards/$', views.openhazards, name='openhazards'),
    url(r'^closedhazards/$', views.closedhazards, name='closedhazards'),
    url(r'^evaluation/(?P<report_no>[\w-]+)/$', views.evaluation, name='evaluation'),
    url(r'^stationReport/(?P<station_id>[\w-]+)/$', views.stationReport, name='stationReport'),
    url(r'^detailedView/(?P<report_no>[\w-]+)/$', views.detailedView, name='detailedView'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^downloads/$', views.downloads, name='downloads'),
    url(r'login_success/$', views.login_success, name='login_success'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)