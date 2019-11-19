from django.conf.urls import url
import django.contrib.auth.views

# from .views import GeneratePDF
# from django.urls import path
#from virtualenv import path

# from .views import Pdf
from . import views
from django.conf import settings
from django.conf.urls.static import static
from  django.contrib.auth import views as auth_views

urlpatterns = [
    # xlsx exports
    url(r'^trainingListxlsx/$', views.trainingListxlsx, name='trainingListxlsx'),
    url(r'^expiredxlsx/$', views.expiredxlsx, name='expiredxlsx'),
    url(r'^untrainedxlsx/$', views.untrainedxlsx, name='untrainedxlsx'),
    # url(r'^searchpdf/$', views.searchpdf, name='searchpdf'),
    url(r'^expired/$', views.expired, name='expired'),
    url(r'^employeeList/$', views.employeeList, name='employeeList'),
    url(r'^trainingList/$', views.trainingList, name='trainingList'),
    url(r'^untrained/$', views.untrained, name='untrained'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^viewRecord/$', views.viewRecord, name='viewRecord'),
    url(r'^search/$', views.search, name='search'),
    url(r'^resources/$', views.resources, name='resources'),
    # url(r'^generate', views.generate, name='generate'),
    url(r'^training_history/(?P<staff_number>[\w-]+)/$', views.training_history, name='training_history'),
    url(r'^getPdf/$', views.getPdf, name='getPdf'),
    url(r'^certificate/(?P<id>[\w-]+)/$', views.certificate, name='certificate'),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),


    #ajax url
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    # url(r'^pdf/$', GeneratePDF.as_view()),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)