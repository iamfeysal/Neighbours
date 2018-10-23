from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # /app/

    url( '^$' , views.home , name='home' ) ,
    url( r'^index/$' , views.Index , name='index' ) ,
    # /app/register
    url( r'^register/$' , views.UserForm.as_view( ) , name='register' ) ,

    # /app/search/
    url( r'^search/' , views.search , name='search' ) ,
    # /app/<project_id>/
    url( r'^(?P<pk>[0-9]+)/$' , views.DetailView.as_view( ) , name='detail' ) ,
    # /app/faq/
    url( '^faq/$' , views.faq , name='faq' ) ,
    # /app/neighbourhood/add/
    url( r'neighbourhood/add/$' , views.NeighbourhoodCreate.as_view( ) , name='neighbourhood-add' ) ,
    # /app/project/add/
    url( r'project/add/$' , views.ProjectCreate.as_view( ) , name='project-add' ) ,
    # /app/business/add/
    url( r'business/add/$' , views.BusinessCreate.as_view( ) , name='business-add' ) ,
    # /app/neighbourhood/3/delete
    url( r'neighbourhood/(?P<pk>[0-9]+)/delete/$' , views.NeighbourhoodDelete.as_view( ) ,
         name='neighbourhood-delete' ) ,
    # /app/project/2/delete
    url( r'project/(?P<pk>[0-9]+)/delete/$' , views.ProjectDelete.as_view( ) , name='project-delete' ) ,

    # /app/neighbourhood/2/update
    url( r'neighbourhood/(?P<pk>[0-9]+)/$' , views.NeighbourhoodUpdate.as_view( ) , name='neighbourhood-update' ) ,
    # /app/project/2/update
    url( r'project/(?P<pk>[0-9]+)/$' , views.ProjectUpdate.as_view( ) , name='project-update' ) ,
]
if settings.DEBUG:
    urlpatterns+=static( settings.MEDIA_URL , document_root=settings.MEDIA_ROOT )
