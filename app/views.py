from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import  authenticate,login
from django.views.generic import View
from .models import *

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'Hood/index.html'
    context_object_name = 'all_project'

    def get_queryset(self):
        return Project.objects.all( )
class DetailView(generic.DetailView):
    model = Project
    template_name = 'Hood/detail.html'


