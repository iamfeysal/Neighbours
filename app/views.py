from django.views import generic
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login
from django.views.generic import View
from django.http import HttpResponse , Http404 , HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from .models import *


# Create your views here.

def home(request):
    return render( request , 'home.html' )


def faq(request):
    return render( request , 'faq.html' )


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
def search(request):
    if request.GET['search']:
        search_term=request.GET.get( "search" )
        hoods=Neighbourhood.objects.filter(name__icontains=search_term )
        message=f"{search_term}"

        return render( request , 'Hood/search.html' , {"message": message , "hoods": hoods} )
    else:
        message="You haven't searched for any item"
        return render( request ,'search.html' , {"message": message} )


class UserForm(View):
    form_class = UserForm
    template_name = 'registration/registration_form.html'


    #dislay blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    #process  form data
    def post(self , request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # clean (normailized) data
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User object if credential are correct
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('index')

        return render( request , self.template_name , {'form': form} )