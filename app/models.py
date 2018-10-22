from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField
from django.core.urlresolvers import reverse


# Create your models here.

class Neighbourhood( models.Model ):
    CITY_CHOICES=(
        ('Nairobi' , 'Nairobi') ,
        ('Machakos' , 'Machakos') ,
        ('KItui' , 'KItui') ,
        ('Garissa' , 'Garissa') ,
        ('Mombasa' , 'Mombasa') ,
        ('Malindi' , 'Malindi') ,
        ('Kisumu' , 'Kisumu') ,
        ('Migori' , 'Migori') ,
        ('Kakamega' , 'Kakamega') ,
        ('Uasingishu' , 'Uasingishu') ,

    )

    name=models.CharField( max_length=300 , null=True )
    description=models.CharField(max_length=500 , null=True)
    location=models.CharField( max_length=100 , choices=CITY_CHOICES )
    population=models.IntegerField( )
    user=models.ForeignKey( User )

    def get_absolute_url(self):
        return reverse( 'detail' , kwargs={'pk': self.pk} )

    def save_hood(self):
        self.save( )

    def delete_hood(self):
        self.delete( )

    @classmethod
    def search_hood(cls , search_term):
        hoods=cls.objects.filter( name__icontains=search_term )
        return hoods

    def __str__(self):
        return self.name


class Business( models.Model ):
    business_name=models.CharField( max_length=30 , null=True )
    user=models.ForeignKey( User , on_delete=models.CASCADE , null=True , related_name="business" )
    neighbourhood=models.ForeignKey( Neighbourhood )
    email_address=models.CharField( max_length=200 , null=True )

    def __str__(self):
        return self.business_name

    def get_absolute_url(self):
        return reverse( 'detail' , kwargs={'pk': self.pk} )


    def save_business(self):
        self.save( )

    @classmethod
    def delete_business_by_id(cls , id):
        businesses=cls.objects.filter( pk=id )
        businesses.delete( )

    @classmethod
    def get_businesses_by_id(cls , id):
        businesses=cls.objects.get( pk=id )
        return businesses

    @classmethod
    def filter_by_location(cls , location):
        businesses=cls.objects.filter( location=location )
        return businesses

    @classmethod
    def search_businesses(cls , search_term):
        businesses=cls.objects.filter( business_name__icontains=search_term )
        return businesses

    @classmethod
    def update_business(cls , id):
        businesses=cls.objects.filter( id=id ).update( id=id )
        return businesses

    @classmethod
    def update_business(cls , id):
        businesses=cls.objects.filter( id=id ).update( id=id )
        return businesses


class Comments( models.Model ):
    comment=models.CharField( max_length=600 )
    user=models.ForeignKey( User )

    def save_comment(self):
        self.save( )

    def delete_comment(self):
        self.delete( )

    def __str__(self):
        return self.comment


class Profile( models.Model ):
    objects=None
    profilePic=models.ImageField( upload_to='profile/' , null=True , blank=True )
    contact=HTMLField( max_length=60 , null=True )
    bio=models.CharField( max_length=60 , blank=True )
    user=models.ForeignKey( User , on_delete=models.CASCADE , related_name='profile' , null=True )
    email=models.TextField( max_length=200 , null=True , blank=True , default=0 )

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save( )

    def delete_profile(self):
        self.delete( )

    @classmethod
    def get_profile(cls):
        profile=Profile.objects.all( )
        return profile

    @classmethod
    def find_profile(cls , search_term):
        profile=cls.objects.filter( user__username__icontains=search_term )
        return profile


class Project( models.Model ):
    title=models.CharField( max_length=300 )
    body=models.TextField( )
    user=models.ForeignKey( User )
    neighbourhood=models.ForeignKey( Neighbourhood )

    def get_absolute_url(self):
        return reverse( 'detail' , kwargs={'pk': self.pk} )

    def save_projects(self):
        self.save( )

    def delete_projects(self):
        self.delete( )

    def __str__(self):
        return self.title


class Join( models.Model ):
    user_id=models.OneToOneField( User )
    hood_id=models.ForeignKey( Neighbourhood )

    def __str__(self):
        return self.user_id


class NewsLetterRecipients( models.Model ):
    name=models.CharField( max_length=30 )
    email=models.EmailField( )
