from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # /app/
    url( r'^$' , views.IndexView.as_view( ) , name='index' ) ,
    # /app/<project_id>/
    url( r'^(?P<pk>[0-9]+)/$' , views.DetailView.as_view( ) , name='detail' ) ,
]
