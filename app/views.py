from django.views import generic
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login
from django.views.generic import View
from django.http import HttpResponse , Http404 , HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.

def home(request):
    return render( request , 'home.html' )


def faq(request):
    return render( request , 'faq.html' )


@login_required( login_url='/accounts/login/' )
def Index(request):
    '''
    Method that fetches all images from all users.
    '''
    date=dt.date.today( )
    profile=Profile.objects.all
    project=Project.objects.all()
    business=Business.objects.all()
    neighbourhood=Neighbourhood.objects.all()
    return render( request , 'Hood/index.html' , {
        "profile": profile ,
        "neighbourhood":neighbourhood,
        "project": project ,
        "business":business,
        "date":date,} )


class DetailView( generic.DetailView ):
    model=Neighbourhood
    template_name='Hood/detail.html'

class ProjectDetail(generic.DetailView):
    model=Project
    template_name = 'Hood/prodetail.html'

class NeighbourhoodCreate( CreateView ):
    model=Neighbourhood
    template_name='Hood/neighbourhood_form.html'
    fields=['name' , 'description' , 'location' , 'population','user']

class ProjectCreate( CreateView ):
    model=Project
    template_name='Hood/project_form.html'
    fields=['title' , 'body' , 'neighbourhood','user']

class BusinessCreate( CreateView ):
    model=Business
    template_name='Hood/business_form.html'
    fields=['business_name' , 'user' , 'neighbourhood','email_address']


class NeighbourhoodUpdate(UpdateView):
    model=Neighbourhood
    template_name = 'Hood/neighbourhood_form.html'
    fields = ['name', 'description','location','population']


class ProjectUpdate(UpdateView):
    model=Project
    template_name = 'Hood/project_form.html'
    fields = ['title', 'body','neighbourhood']



class NeighbourhoodDelete(DeleteView):
    model=Neighbourhood
    success_url = reverse_lazy('index')


class ProjectDelete(DeleteView):
    model=Project
    success_url = reverse_lazy('index')


