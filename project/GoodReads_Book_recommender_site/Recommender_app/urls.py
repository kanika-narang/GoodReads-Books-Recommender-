from django.conf.urls import url
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recommend/$', views.recommend, name='recommend'),
    url(r'^collaborative/$', views.collaborative, name='collaborative'),
    url(r'^content/$', views.content, name='content'),
    url(r'^matrix/$', views.matrix, name='matrix'),
    url(r'^popularity/$', views.popularity, name='popularity'),


    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)