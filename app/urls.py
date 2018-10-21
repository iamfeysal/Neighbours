from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # /app/
    url( '^$' , views.home , name='home' ) ,
    url( r'^index/$' , views.IndexView.as_view( ) , name='index' ) ,
    # /app/<project_id>/
    url( r'^(?P<pk>[0-9]+)/$' , views.DetailView.as_view( ) , name='detail' ) ,
]
if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL , document_root=settings.MEDIA_ROOT )
