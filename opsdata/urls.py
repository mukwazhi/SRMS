
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from  django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^statistics', views.statistics, name='statistics'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)